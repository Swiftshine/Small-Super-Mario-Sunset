import os

def join_files(input_files, output_file):
    with open(output_file, 'wb') as outfile:
        for filename in input_files:
            with open(filename, 'rb') as infile:
                outfile.write(infile.read())


def main():

    # go through every file in /bfsar/ and join them together
    input_files = list()
    for root, dirs, files in os.walk("bfsar"):
        for file in files:
            if ".dat" in file:
                input_files.append(os.path.join(root, file))

    print(f"Joining {len(input_files)} files...")
    join_files(input_files, "content/CAFE/sound/cafe_redpro_sound.bfsar")
    print("Done!")
if __name__ == "__main__":
    main()