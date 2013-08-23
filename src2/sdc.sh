control_c()
# run if user hits control-c
{
  echo -en "\n*** Ouch! Exiting ***\n"
  sudo airmon-ng stop mon0
  sleep 3

  exit
}
trap control_c SIGINT

sudo airmon-ng start wlan0
sleep 3
sudo python scapyprobes.py & #> /dev/null 2>&1&
python APFinder.py
sleep 3
sudo airmon-ng stop mon0


