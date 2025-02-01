from utils.system import System

def main():
    try:
        AVANT = System()
        AVANT.folder_structure_check()
        AVANT.check_q3_installation() 
        AVANT.init()
        while True:
            choice = AVANT.main_menu()
            match(choice):
                case 1:
                    AVANT.manage_avant_projects()
                case 2:
                    AVANT.gen_map_data()
                case 3:
                    AVANT.gen_demo_files()
                case 4:
                    AVANT.gen_mme_projs()
                case 5:
                    AVANT.gen_nle_data()
                case 6:
                    AVANT.how_to_use()
                case 7:
                    AVANT.show_credits()
                case 8:
                    AVANT.exit_avant()
    except KeyboardInterrupt:
        AVANT.exit_avant()

if __name__ == "__main__":
    main()
