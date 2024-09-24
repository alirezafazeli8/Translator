from translate import Translator

# User Guide
print(
    """
      
      Welcome To Python Text Translator
      
            We support many languages
            
            pleas support me in github and linkedin
                - github : github.com/alirezafazeli8
                - linkedin : linkedin.com/in/alirezafazeli
                
        --------------------------------------------------
        
        Note : First of all, put your txt file in the document folder, and after running Python enter just your file name without .txt 
        
        --------------------------------------------------
        
        List Of Target Language : 
        
        fa - en - zh - ar - az - de - es - fr 
        hy - it - ja - nl - no - pt - ru - tr
        
        
        --------------------------------------------------
       
      """
)

# get just file name without .txt from user
user_file = input("Pleas Enter File Name : ")
# get iso code
target_language = input("Pleas Enter Your Target Language (default : Persian - fa ) : ")
# filepath
file_path = f"./document/{user_file}.txt"

try:
    # open main file should translate
    with open(file_path, mode="r", encoding="utf-8") as curr_file:
        # create new translated file path
        new_file_path = f"./document/translate-{user_file}.txt"
        # write translated text to new file
        with open(new_file_path, mode="a", encoding="utf-8") as new_trans_file:
            # make translator for target language
            translator = Translator(to_lang=target_language or "fa")
            print("Translating In Progress ...")
            # write original text and translated text
            for line_text in curr_file.readlines():
                new_trans_file.write(
                    f"""
{line_text}\n
{translator.translate(line_text)}\n
                    """
                )

            print("-----------DONE--------------")
            # print address of  translated file
            print(f"Pleas Open : '{new_file_path}'")
# handle file notfound error
except FileNotFoundError:
    print("File Not Found. Run App Again !")
# handle IO error
except IOError:
    print("Problem In Operation ...")
# handle Internet Connection error
except:
    print("Internet Connection Error. Try Again :)")
