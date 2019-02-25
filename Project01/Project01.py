"""    python Project_01_edited.py pragya.fq Sp2.fq 33 25   """

import itertools
from sys import argv


def get_read(fq):

    myfile = list(itertools.islice(fq, 4))

    if myfile:

        seq_id = myfile[0].strip()
        nucleotide_seq = myfile[1].strip()
        sec_id = myfile[2].strip()
        scores = myfile[3].strip()
        # print(seq_id, nucleotide_seq, sec_id, scores)
    else:
        return False

    return [seq_id, nucleotide_seq, sec_id, scores]


def trim_read_front(read, min_score, min_size):

    seq_id = read[0]
    nuc_seq = read[1]
    sec_id = read[2]
    scores = read[3]

    # numb_scores = []
    # for s in scores:
    # numb_scores.append(ord(s) - 33)
    # its the same code for the one commented above
    numb_scores = [ord(s) - 33 for s in scores]

    index = 0
    for j in numb_scores:
        if j >= int(min_score):
            break
        index += 1

    nuc_seq = nuc_seq[index:]
    out_score = scores[index:]

    if len(out_score) < int(min_size):
        # print('false')
        return False
        # print(False)

    trimmed_read = [seq_id, nuc_seq, sec_id, out_score]

    return trimmed_read
    # print(trimmed_read)


def main(argv):
    Script, input_file, out_file, min_score, min_size = argv
    total_reads = 0
    total_trimmed_reads = 0
    total_reads_kept = 0

    with open(input_file, "r") as file_handle:
        with open(out_file, "w") as output_file:

            # count = 0 (the program is not printing all the trimmed reads which has been asked to print,
                         #but is printing this much of command because the file pointer is already at the end of the file )
            # for every_read in file_handle:
            #     count += 1
            # print("total number of reads is:", count/4)

            read = get_read(file_handle)



            while read:
                #print(read)
                total_reads += 1  # this counter is here because if its below then
                # it would also count the last time read is called which would return false
                trim = trim_read_front(read, min_score, min_size)
                print(trim)
                if trim:
                    total_trimmed_reads += 1
                    final_trim = f"{trim[0]}\n {trim [1]} \n {trim[2]}\n {trim[3]} \n"
                    output_file.writelines(final_trim)
                total_reads_kept = total_reads - total_trimmed_reads
                read = get_read(file_handle)

    print(f'Total Reads: {total_reads}')
    print(f"Total number of trimmed reads kept: {total_trimmed_reads}")
    print(f"Total number of reads discarded: {total_reads_kept}")

main(argv)
