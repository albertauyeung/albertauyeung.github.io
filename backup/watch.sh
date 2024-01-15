#/bin/zsh
python3 -m http.server &
while true
do
    ./build.sh
    sleep 5
done

