import configparser
import pandas as pd

def read_config_details(cfg_filepath):
    config = configparser.RawConfigParser()
    print('file path ',cfg_filepath)
    config.read(cfg_filepath)
    details_dict = dict(config.items('APP'))

    print('details ::::::',details_dict)
    return details_dict


# read_csv : This function will read data from csv
def read_csv(filepath):
    driver_file_data = pd.read_csv(filepath, header=0)
    return driver_file_data


# get_execution_details : This will fetch Test Data in the form of list for given test case ID
def get_execution_details(filepath,testcase_name):
    testcase_details = read_csv(filepath)
    print('csv data ::::',testcase_details)
    print(type(testcase_details))
    search_criteria_list = 'N'
    # Filter CSV Data with RunFlag to execute testcase which are marked as Y
    # df_testdata = testcase_details[testcase_details['RunFlag'] == 'Y']
    # df_testdata=testcase_details
    # if df_testdata.empty:
    #   print('Run Flag for all testcases are marked as N ')
    # else:
    #     testcase_data = df_testdata[df_testdata['FunctionName'] == testcase_name]
    #     if not testcase_data.empty:
    #         testdata = testcase_data[testcase_data.FunctionName == testcase_name].Testdata.item()
    #         search_criteria_list = testdata.split('|')
    #
    # return search_criteria_list