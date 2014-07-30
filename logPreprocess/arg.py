#! /usr/bin/python
# author:    nullne
# email:     co.crary@gmail.com
# Do:        output script instruction  
def main():
    import argparse

    parser = argparse.ArgumentParser(description="preprocess the file and store the result in res directory")
    #positional arguments
    parser.add_argument("filename", help="the location of the file need to be preprocessed")

    #optional arguments
    parser.add_argument("-c", "--config", default="matchPatterns.cfg", help="Change  to your own config file if needed,or use the default config file: matchPatterns.cfg")
    #parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
    #parser.add_argument("-f", "--fuck", help="", action="count", default=0)
    #parser.add_argument("-i", "--int", help="", type=int, choices=[0,1,2])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
