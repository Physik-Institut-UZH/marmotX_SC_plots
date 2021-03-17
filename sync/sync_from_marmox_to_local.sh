while true; do
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/pdata /home/marmotx/slowcontrol-2021/data/pdata
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/tdata /home/marmotx/slowcontrol-2021/data/tdata
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/vdata /home/marmotx/slowcontrol-2021/data/vdata
sleep 120
done 	
