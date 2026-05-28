BASE_PATH = '/Volumes/salesdatalakehouse/bronze/sourcesystems'

INGESTION_CONFIG = [
    # CRM source files
    {
        'source': 'crm',
        'path': f'{BASE_PATH}/CRM/cust_info.csv',
        'table': 'crm_cust_info_raw'
    },
    {
        'source': 'crm',
        'path': f'{BASE_PATH}/CRM/prd_info.csv',
        'table': 'crm_prd_info_raw'
    },
    {
        'source': 'crm',
        'path': f'{BASE_PATH}/CRM/sales_details.csv',
        'table': 'crm_sales_details_raw'
    },
    # ERP source files
    {
        'source': 'erp',
        'path': f'{BASE_PATH}/ERP/CUST_AZ12.csv',
        'table': 'erp_cust_az12_raw'
    },
    {
        'source': 'erp',
        'path': f'{BASE_PATH}/ERP/LOC_A101.csv',
        'table': 'erp_loc_a101_raw'
    },
    {
        'source': 'erp',
        'path': f'{BASE_PATH}/ERP/PX_CAT_G1V2.csv',
        'table': 'erp_px_cat_g1v2_raw'
    }
]
