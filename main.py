import pandas as pd
import utils
import config
import matplotlib.pyplot as plt


dataset_path_output = './outputFile/'


def main():
    # Part 1 : Load dataset
    candidates_house_of_commons_df, representatives_df, representatives_house_of_commons_df, \
    quebec_assemblee_nationale_df, conseil_municipal_de_montreal_df = utils.prepare_dataset()

    # Part 2 : Data Process
    # 2.1 Check Candidates : House of Commons
    col_candidates_house_of_commons_df = ['District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name' ]
    candidates_house_of_commons_df = utils.proces_data(candidates_house_of_commons_df, col_candidates_house_of_commons_df, 'Candidates : House of Commons')

    # 2.2 Check Representatives : All elected officials
    col_representatives_df = ['Organization', 'District name', 'Primary role', 'Name', 'First name', 'Last name','Gender', 'Party name', 'Office type']
    representatives_df = utils.proces_data(representatives_df, col_representatives_df, 'Representatives : All elected officials')

    # 2.3 Check Representative : House of Commons
    col_representatives_house_of_commons_df = ['District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name', 'Office type']
    representatives_house_of_commons_df = utils.proces_data(representatives_house_of_commons_df, col_representatives_house_of_commons_df, 'Representative : House of Commons')

    # 2.4 Check Provincial legislatures : Assemblée nationale du Québec
    col_quebec_assemblee_nationale_df = ['District name', 'Primary role', 'Name', 'First name', 'Last name', 'Party name', 'Office type']
    quebec_assemblee_nationale_df= utils.proces_data(quebec_assemblee_nationale_df, col_quebec_assemblee_nationale_df, 'Provincial legislatures : Assemblée nationale du Québec')

    # 2.5 Check Quebec councils : Conseil municipal de Montréal
    col_conseil_municipal_de_montreal_df = ['District name', 'Primary role', 'Name', 'First name', 'Last name', 'Gender', 'Party name', 'Office type']
    conseil_municipal_de_montreal_df = utils.proces_data(conseil_municipal_de_montreal_df, col_conseil_municipal_de_montreal_df, 'Quebec councils : Conseil municipal de Montréal')

    # Part 3 : Data Analysis
    # 3.1 Analyze Candidates : House of Commons
    # Group by 'Party name'
    title_pic = 'Candidates house of commons'
    save_path = dataset_path_output +'Candidates house of commons.png'
    top10 = 0
    utils.data_ana(candidates_house_of_commons_df, 'Party name', title_pic, save_path, top10)

    # Group by 'District name'
    title_pic = 'Top 10 District of Candidates <House of Commons>'
    save_path = dataset_path_output + 'Top 10 District of Candidates House of Commons.png'
    top10 = 1
    utils.data_ana(candidates_house_of_commons_df, 'District name', title_pic, save_path, top10)

    # 3.2 Analyze Representatives : All elected officials
    # Group by 'Organization'
    title_pic = 'Top 10 Organizations of Representatives <All elected officials>'
    save_path = dataset_path_output + 'Top 10 Organizations of Representatives All elected officials.png'
    top10 = 1
    utils.data_ana(representatives_df, 'Organization', title_pic, save_path, top10)

    # Group by 'District name'
    title_pic = 'Top 10 Districts of Representatives <All elected officials>'
    save_path = dataset_path_output + 'Top 10 districts of representatives of All elected officials.png'
    top10 = 1
    utils.data_ana(representatives_df, 'District name', title_pic, save_path, top10)

    # Group by 'Primary role'
    title_pic = 'Primary Role of Representatives <All elected officials>'
    save_path = dataset_path_output + 'Primary role of representatives of All elected officials.png'
    top10 = 0
    utils.data_ana(representatives_df, 'Primary role', title_pic, save_path, top10)

    # Group by 'Office type'
    title_pic = 'Office Type of Representatives <All elected officials>'
    save_path = dataset_path_output + 'Office type of representatives of All elected officials.png'
    top10 = 0
    utils.data_ana(representatives_df, 'Office type', title_pic, save_path, top10)

    # 3.3 Analyze Representatives : House of Commons
    # Group by 'Party name'
    title_pic = 'Party name of Representatives <House of Commons>'
    save_path = dataset_path_output + 'Party name of Representatives House of Commons.png'
    top10 = 0
    utils.data_ana(representatives_house_of_commons_df, 'Party name', title_pic, save_path, top10)

    # 3.4 Analyze Provincial legislatures : Assemblée nationale du Québec
    # Group by 'Party name'
    title_pic = 'Party name of legislatures <Assemblée nationale du Québec>'
    save_path = dataset_path_output + 'Party name of legislatures Assemblée nationale du Québec.png'
    top10 = 0
    utils.data_ana(quebec_assemblee_nationale_df, 'Party name', title_pic, save_path, top10)

    # Group by 'Office type'
    title_pic = 'Office type of legislatures <Assemblée nationale du Québec>'
    save_path = dataset_path_output + 'Office type of legislatures Assemblée nationale du Québec.png'
    top10 = 0
    utils.data_ana(quebec_assemblee_nationale_df, 'Office type', title_pic, save_path, top10)

    # 3.5 Analyze Quebec councils : Conseil municipal de Montréal
    # Group by 'Primary role'
    title_pic = 'Primary role of councils of Conseil municipal de Montréal'
    save_path = dataset_path_output + 'Primary role of councils of Conseil municipal de Montréal.png'
    top10 = 0
    utils.data_ana(conseil_municipal_de_montreal_df, 'Primary role', title_pic, save_path, top10)

    # Group by 'Party name'
    title_pic = 'Party name of councils of Conseil municipal de Montréal'
    save_path = dataset_path_output + 'Party name of councils of Conseil municipal de Montréal.png'
    top10 = 0
    utils.data_ana(conseil_municipal_de_montreal_df, 'Party name', title_pic, save_path, top10)

    # Group by 'Gender'
    title_pic = 'Gender of councils of Conseil municipal de Montréal'
    save_path = dataset_path_output + 'Gender of councils of Conseil municipal de Montréal.png'
    top10 = 0
    utils.data_ana(conseil_municipal_de_montreal_df, 'Gender', title_pic, save_path, top10)



if __name__=="__main__":
    main()