"""
downloads files from allas' buckets
"""

import pandas as pd

import os
from pathlib import Path


def get_conn():
    """get connection to allas"""
    # noinspection PyUnresolvedReferences
    from keystoneauth1 import session
    # noinspection PyUnresolvedReferences
    from keystoneauth1.identity import v3
    # noinspection PyUnresolvedReferences
    import swiftclient
    _authurl = os.environ['OS_AUTH_URL']
    _auth_version = os.environ['OS_IDENTITY_API_VERSION']
    _user = os.environ['OS_USERNAME']
    _key = os.environ['OS_PASSWORD']
    _os_options = {
        'user_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
        'project_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
        'project_name': os.environ['OS_PROJECT_NAME']
    }

    conn = swiftclient.Connection(
        authurl=_authurl,
        user=_user,
        key=_key,
        os_options=_os_options,
        auth_version=_auth_version
    )
    return conn


def get_df(bucket_name, conn, filter_):
    """gets the list of available objects"""
    resp_headers, containers = conn.get_account()
    # %%
    pd.DataFrame(containers)
    # %%
    df = pd.DataFrame(conn.get_container(bucket_name, prefix=filter_)[1])

    if filter_ is None:
        return df
    # %%
    # %%
    # noinspection SpellCheckingInspection
    # df1 = df[df['name'].str[:10] == filter_].copy()
    df1 = df
    df1['time'] = pd.to_datetime(df1['name'].str[-19:],
                                 format='%Y-%m-%d_%H:%M:%S')
    df1 = df1.set_index('time')
    return df1


def get_download_file_list(avail_file_list):
    dfs = []
    for a1 in avail_file_list:
        # a1 = run_dir + f'/AVAILABLE0{i + 1}'
        df = pd.read_csv(
            a1, skiprows=3, names=['a', 'b', 'c', 'd', 'e'],
            sep='\s+',
            quotechar="'",
        )['c']
        df = df.drop_duplicates()
        dfs.append(df)
    dfF = pd.concat(dfs).reset_index(drop=True)
    return dfF


def download_files(*, df, down_path, bucket, conn):
    """downloads the files from the bucket at allas"""
    for w in df:
        path_out = Path(down_path) / w
        print(path_out)
        with open(path_out, 'bw') as f:
            a, b = conn.get_object(bucket, w)
            f.write(b)


def save_download_script(*, dir_out, df, bucket, path_script):
    d1 = df.apply(
        lambda x: f'swift download -o {Path(dir_out) / x} {bucket} {x}'
    )
    d1.to_csv(path_script, header=False, index=False)
