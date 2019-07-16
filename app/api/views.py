# -*- coding: utf-8 -*-
from flask import render_template, request, session, current_app
from werkzeug.utils import secure_filename
import tempfile
import shutil
import os
from ..decorator import login_required
from ..untils import AnalysisNessus
from . import api
from ..models import db


@api.route('/nessus_analysis', methods=['POST'])
@login_required
def nessus_analysis():
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
    for key in result:
        df = result[key]
        risk = analysis.get_values_of_column(df, 'Risk')
        plugin_id = analysis.get_values_of_column(df, 'Plugin ID')
        name = analysis.get_values_of_column(df, 'Name')
        zipped = zip(risk, plugin_id, name)
        result[key] = zipped

    return render_template('nessus_result.html', result=result)

