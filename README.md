# PyPo - Python based playout
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdigris%2Fobp-playout.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdigris%2Fobp-playout?ref=badge_shield)

 
PyPo acts as a gateway between web API/RabbitMQ and Liquidsoap.


## Installation

Steps below assume using Debian 9.x (Stretch)


## Notes

Scheduler data from the Openbroadcast platform is in timezone format and not UTC. The system running the playout 
has to be configured with the corresponding timezone. (CEST)


[Scheduler API](http://dev.openbroadcast.org/api/v1/abcast/base/get-schedule/?format=json)



## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdigris%2Fobp-playout.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdigris%2Fobp-playout?ref=badge_large)