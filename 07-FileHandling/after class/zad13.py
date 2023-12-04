# 13.	The following program displays the contents of a file, line by line:
# f = open("filename.txt")
# for line in f:
#      print(line, end="")
# f.close()
# Rewrite the program using the "with ..." as construct. Then check that the program is working properly.

def main() -> None:
      # with open("filename.txt", 'r') as f:
      #       for line in f.readlines():
      #             print(line, end=' ')

      try:
            with open("filename.txt", 'r') as f:
                  for line in f.readlines():
                        print(line, end=' ')
      except:
        print("Plik nie został znaleziony.")

if __name__ == '__main__':
      main()