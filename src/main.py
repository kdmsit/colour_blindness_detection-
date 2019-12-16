import numpy as np
import pickle
def data_load(chrx_ref_seq_path,bwt_last_col_path,map_file_path,read_file_path):
    ref_sequence = np.loadtxt(chrx_ref_seq_path, dtype=str)
    bwt_last_col_data = np.loadtxt(bwt_last_col_path, dtype=str)
    # bwt_index_map = np.loadtxt(map_file_path, dtype=str)
    read_data = np.loadtxt(read_file_path, dtype=str)
    return ref_sequence,bwt_last_col_data,read_data

if __name__ == "__main__":

    # Data Load Section
    chrx_ref_seq_path='../data/chrX.fa'
    bwt_last_col_path='../data/chrX_last_col.txt'
    map_file_path="../data/chrX_map.txt"
    read_file_path="../data/reads"
    ref_sequence,bwt_last_col_data,read_data=\
        data_load(chrx_ref_seq_path, bwt_last_col_path, map_file_path, read_file_path)
    print("Done")
