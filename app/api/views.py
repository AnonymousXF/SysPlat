# -*- coding: utf-8 -*-
from flask import render_template, request, session, current_app
from werkzeug.utils import secure_filename
import json
import tempfile
import shutil
import os
from ..decorator import login_required
from ..utils import AnalysisNessus
from . import api
from ..models import db, RecordInfo


@api.route('/nessus_analysis', methods=['POST'])
@login_required
def nessus_analysis():
    """
    分析上传的csv格式的Nessus扫描结果
    :return:
    """
    # 获取请求中上传的文件和参数
    f = request.files.get('file')
    level = request.values.get('level')

    # 检查上传的文件名
    filename = secure_filename(f.filename)
    if not filename.endswith('csv'):
        return u'分析失败，请上传csv格式的扫描结果！'

    # 创建临时目录，保存上传的文件，用于后续分析
    tmpdir = tempfile.mkdtemp()
    f.save(os.path.join(tmpdir, filename))

    # 创建AnalysisNessus对象，删除临时目录和临时文件
    analysis = AnalysisNessus(os.path.join(tmpdir, filename), level)
    shutil.rmtree(tmpdir)

    # 返回分析结果
    result = analysis.analysis()
    for key in result.keys():
        df = result[key]
        risk = analysis.get_values_of_column(df, 'Risk')
        plugin_id = analysis.get_values_of_column(df, 'Plugin ID')
        name = analysis.get_values_of_column(df, 'Name')
        zipped = zip(risk, plugin_id, name)
        result[key] = zipped

    return render_template('nessus_result.html', result=result)


@api.route('/add_record', methods=['POST'])
def add_record():
    """
    添加漏洞记录
    :return:
    """
    # 获取请求中的参数
    scan_tool = request.values.get('scanTool')
    vul_level = request.values.get('vulLevel')
    vul_name = request.values.get('vulName')
    nessus_plugin_id = request.values.get('nessusPluginID')
    vul_link = request.values.get('vulLink')
    detail_info = request.values.get('detailInfo')
    project = request.values.get('project')
    if not all([vul_name, detail_info]):
        return json.dumps({'warning': u'请填写必填项！'})
    try:
        if nessus_plugin_id != '':
            new_record = RecordInfo(tool_for_vulnerability=scan_tool,
                                    vulnerability_name=vul_name,
                                    vulnerability_level=vul_level,
                                    nessus_pluginID=int(nessus_plugin_id),
                                    detail_info=detail_info,
                                    record_project=project)
            db.session.add(new_record)
            db.session.commit()
        else:
            new_record = RecordInfo(tool_for_vulnerability=scan_tool,
                                    vulnerability_name=vul_name,
                                    vulnerability_level=vul_level,
                                    vulnerable_link=vul_link,
                                    detail_info=detail_info,
                                    record_project=project)
            db.session.add(new_record)
            db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return json.dumps({'failed': '添加漏洞信息失败！'})
    return json.dumps({'success': '添加漏洞信息成功！'})
