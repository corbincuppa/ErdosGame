while [[ "$#" -gt 0 ]]; do
    case $1 in
        --image_folder)
            IMAGE_FOLDER="$2"
            if [ -e "$2" ]
            then
            sleep .5
            else
            mkdir $IMAGE_FOLDER
            fi	
            shift 2
            ;;

        --export)
            IMAGE_FORMAT="$2"
            python3 export.py "startingFile.json" $IMAGE_FORMAT
            mv "EndGameAliceGraph.$IMAGE_FORMAT" $IMAGE_FOLDER
            mv "EndGameBobGraph.$IMAGE_FORMAT" $IMAGE_FOLDER
            shift 2
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done