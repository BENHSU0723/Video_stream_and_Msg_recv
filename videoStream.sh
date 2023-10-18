LIST=""
sudo -E CONVERT_LOG=/home/demo/log/convert.log LD_PRELOAD=/home/demo/ATSSS-UE-code/libconvert-MPTCP/build/libconvert_client.so SYN_PARAM_PATH=/sys/module/syn_rfc8803/parameters python3 client.py &
LIST+=($!)
# sudo -E CONVERT_LOG=/home/demo/log/convert.log LD_PRELOAD=/home/demo/ATSSS-UE-code/libconvert-MPTCP/build/libconvert_client.so SYN_PARAM_PATH=/sys/module/syn_rfc8803/parameters python3 client2.py &
# LIST+=" "
# LIST+=($!)

echo $LIST > runningP.txt

