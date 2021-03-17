while true; do
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/pdata/2* ../Data/pdata
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/tdata/2* ../Data/tdata
rsync -h -v -r -P -t marmotx@marmotx.physik.uzh.ch:/home/atp/marmotx/slowcontrolxl/data/vdata/2* ../Data/vdata
sleep 120
done
