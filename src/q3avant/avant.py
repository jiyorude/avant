from utils.system import System

def main():
    try:
        AVANT = System()
        AVANT.init()
        while True:
            choice = AVANT.main_menu()
            match(choice):
                case 1:
                    AVANT.gen_map_data()
                case 2:
                    AVANT.gen_demo_files()
                case 3:
                    AVANT.gen_mme_projs()
                case 4:
                    AVANT.gen_nle_data()
                case 5:
                    AVANT.how_to_use()
                case 6:
                    AVANT.credits()
                case 7:
                    AVANT.exit_avant()
    except KeyboardInterrupt:
        AVANT.exit_avant()

if __name__ == "__main__":
    main()
