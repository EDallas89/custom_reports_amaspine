# -*- coding: utf-8 -*-
{
    'name': "Custom Reports Ama Spine",
    'summary': """
        Add custom reports templates for Ama Spine""",
    'author': "Aresoltec Canarias S.L.",
    'website': "https://www.aresoltec.com",
    'category': 'Reports',
    'version': '0.1',
    'depends': ['purchase'],
    'data': [
        'report/purchase_reports.xml',
        'report/purchaseorder_document_main.xml',
        #'report/purchaseorder_document_sin_precios_amaspine.xml',
    ],
}
