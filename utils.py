import pandas as pd
import config
import matplotlib.pyplot as plt


def prepare_dataset():
    """

    :return:
    """
    candidates_house_of_commons_df = pd.read_csv(config.candidates_house_of_commons_file, encoding='cp1252')
    representatives_df = pd.read_csv(config.representatives_file, encoding='ISO-8859-1')
    representatives_house_of_commons_df = pd.read_csv(config.representatives_house_of_commons_file, encoding='cp1252')
    quebec_assemblee_nationale_df = pd.read_csv(config.quebec_assemblee_nationale_file, encoding='ISO-8859-1')
    conseil_municipal_de_montreal_df = pd.read_csv(config.conseil_municipal_de_montreal_file, encoding='ISO-8859-1')

    return candidates_house_of_commons_df, representatives_df, representatives_house_of_commons_df, quebec_assemblee_nationale_df, conseil_municipal_de_montreal_df


def proces_data(dataframe_orig, col_inuse, name_df):
    """

    :param dataframe_orig:
    :param col_inuse:
    :param name_df:
    :return:
    """
    print('First 5 rows of "{}" original raw data:'.format(name_df))
    print(dataframe_orig.head())
    print('General information of "{}" original raw data:'.format(name_df))
    print(dataframe_orig.info())
    # select columns in use
    dataframe_keep = dataframe_orig[col_inuse]
    print('DataFrame in use of "{}":'.format(name_df))
    print(dataframe_keep.head())

    return dataframe_keep


def data_ana(dataframe_g, col_gb, title_pic, save_path, top10):
    """

    :param dataframe_g:
    :param col_gb:
    :param title_pic:
    :param save_path:
    :param Top10:
    :return: NULL
    """
    if top10 == 0:
        serr = groupby_ascent(dataframe_g, col_gb)
    else:
        serr = get_top_10(dataframe_g, col_gb)

    draw_barh(serr, title_pic, save_path)


def groupby_ascent(dataframe_g, col_gb):
    """

    :param dataframe_g:
    :param col_gb:
    :return: serr
    """
    obj = dataframe_g.groupby(col_gb)
    serr = pd.Series(obj.size()).sort_values(ascending=True)

    return serr


def get_top_10(dataframe_g, col_gb):
    """

    :param dataframe_g:
    :param col_gb:
    :return: serr
    """
    obj = dataframe_g.groupby(col_gb)
    serr = pd.Series(obj.size()).sort_values(ascending=True)
    serr = serr[len(serr) - 10:len(serr)]

    return serr


def draw_barh(serr, title_pic, save_path):
    """

    :param serr:
    :param title_pic:
    :param save_path:
    :return: NULL
    """
    row_name = list(serr.index)
    row_name.reverse()

    fig, ax = plt.subplots(figsize=(10,5))
    b = ax.barh(serr.index, serr.values, color='#6699CC')

    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y()+rect.get_height()/2, '%d' %
                int(w), ha='left', va='center')

    ax.set_yticks(range(len(row_name)))
    ax.set_yticklabels(list(serr.index))

    plt.xticks(())

    plt.title(title_pic, loc='center', fontsize='15',
              fontweight='bold')
    plt.savefig(save_path)
    plt.show()


