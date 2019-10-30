$(function () {
    var dom = document.getElementById("container");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    var symbolSize = 20;
    var data = [[],
        []];
    var linelist = ["a", "b"]
    var points = [];

    option = {
        title: {
            text: '模拟车辆动态行驶路径'
        },
        tooltip: {
            formatter: function (params) {
                var data = params.data || [0, 0];
                return data[0].toFixed(2) + ', ' + data[1].toFixed(2);
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            min: 0,
            max: 1000,
            type: 'value',
            axisLine: {onZero: false}
        },
        yAxis: {
            min: 0,
            max: 1000,
            type: 'value',
            axisLine: {onZero: false}
        },
        series: [
            {
                id: linelist[0],
                type: 'line',
                smooth: true,
                color: '#00ef00',
                symbolSize: symbolSize,
                data: data[0]
            },
            {
                id: linelist[1],
                type: 'line',
                smooth: true,
                color: '#ff0000',
                symbolSize: symbolSize,
                data: data[1]
            }
        ]
    };

    var zr = myChart.getZr();


    zr.on('click', function (params) {
        var pointInPixel = [params.offsetX, params.offsetY];
        var pointInGrid = myChart.convertFromPixel('grid', pointInPixel);

        if (myChart.containPixel('grid', pointInPixel)) {
            data.push(pointInGrid);

            myChart.setOption({
                series: [{
                    id: 'a',
                    data: data,
                }]
            });
        }
    });

    zr.on('mousemove', function (params) {
        var pointInPixel = [params.offsetX, params.offsetY];
        zr.setCursorStyle(myChart.containPixel('grid', pointInPixel) ? 'copy' : 'default');
    });

    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    var sock = null;
    var serversocket = "ws://127.0.0.1:8080/wsocket";
    sock = new WebSocket(serversocket);
    sock.onopen = function () {
        console.log("connect to " + serversocket);
    }
    sock.onclose = function (e) {
        console.log("connect closed(" + e.code + ")");
    }

    sock.onmessage = function (e) {
        console.log("message recevice:" + e.data);
        //var redata = eval(e.data);
        var redata = jQuery.parseJSON(e.data);
        var pointlist = redata.message

        addpoint(pointlist)
    }

    function send() {
        var smsg = "123456";
        sock.send(smsg);
    }

    function addpoint(params) {
        for (var i = 0; i < params.length; i++) {

            var pointInPixel = [params[i].offsetX, params[i].offsetY];
            var pointInGrid = myChart.convertFromPixel('grid', pointInPixel);

            if (myChart.containPixel('grid', pointInPixel)) {
                data[i].push(pointInGrid);
                myChart.setOption({
                    series: [{
                        id: linelist[i],
                        data: data[i]
                    }]
                });
            }
        }

    }

})
