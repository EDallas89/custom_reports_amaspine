# -*- coding: utf-8 -*-
{
    'name': "Custom Reports Ama Spine",
    'summary': """
        Add custom reports templates for Ama Spine""",
    'author': "Aresoltec Canarias S.L.",
    'website': "https://www.aresoltec.com",
    'category': 'Reports',
    'version': '0.1',
    'depends': ['purchase', 'sale'],
    'data': [
        'report/purchase_reports.xml',
        'report/report_purchaseorder_document_sin_precios_amaspine.xml',
        'report/report_invoice_document_con_firma_amaspine.xml',
    ],
}
