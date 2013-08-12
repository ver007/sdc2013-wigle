control_c()
# run if user hits control-c
{
  echo -en "\n*** Ouch! Exiting ***\n"
  sleep 1
  sudo airmon-ng stop mon0
  exit
}
trap control_c SIGINT

sudo airmon-ng start wlan0
sudo python scapyprobes.py&
python APFinder.py
sudo airmon-ng stop mon0


