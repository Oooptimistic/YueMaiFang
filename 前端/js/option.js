data = $.get('http://127.0.0.1:5000/task1')
gdJson = $.get('https://geo.datav.aliyun.com/areas_v3/bound/440000_full.json')
// 背景地图
$.when(gdJson, data).done( function (gdJson, data) {
  var myCharts = echarts.init(document.querySelector('.cen-top'));
    echarts.registerMap('GD', gdJson[0]);
    option = {
        title: {
            text:"市级房源数量地图",
          textStyle: {
            color: "rgba(255, 255, 255, 1)"
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}{c}套房源',
          textStyle:{
            fontSize:15
          }
        },
        toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {}
          }
        },
        visualMap: {
          min: 0,
          max: 1000,
          text: ['High', 'Low'],
          realtime: true,
          calculable: false,
          inRange: {
            color: ['lightskyblue', 'yellow', 'orangered']
          }
        },
        series: [
          {
            type: 'map',
            map: 'GD',
            label: {
              show: true
            },
            data: data[0]
          }
        ]
      }
    myCharts.setOption(option)
})

// 堆叠条形图
$.get('http://127.0.0.1:5000/task2').done(function (data) {
  var myCharts = echarts.init(document.querySelector('.cen-bottom .charts'));
    option = {
        tooltip : {
            trigger: 'axis',
            axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            top: '25%',
            right: '3%',
            left: '10%',
            bottom: '10%'
        },
        legend: {
            data:[data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[6][0],data[7][0],data[8][0],data[9][0],data[10][0],data[11][0],data[12][0],data[13][0],data[14][0],data[15][0]],
            textStyle : {
                color : '#ffffff',

            }
        },
        calculable :false,
        xAxis : [
            {
                type : 'value',
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: '#fff'
                    }
                },
                splitLine:{
                    lineStyle:{
                        color:['#f2f2f2'],
                        width:0,
                        type:'solid'
                    }
                }

            }
        ],
        yAxis : [
            {
                type : 'category',
                data : ['在售', '待售', '售完'],
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: '#fff'
                    }
                },
                splitLine:{
                    lineStyle:{
                        width:0,
                        type:'solid'
                    }
                }
            }
        ],
        series : [
            {
                name:data[0][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[0][1]
            },
            {
                name:data[1][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[1][1]
            },
            {
                name:data[2][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[2][1]
            },
            {
                name:data[3][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[3][1]
            },
            {
                name:data[4][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[4][1]
            },
            {
                name:data[5][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[5][1]
            },
            {
                name:data[6][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[6][1]
            },
            {
                name:data[7][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[7][1]
            },
            {
                name:data[8][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[8][1]
            },
            {
                name:data[9][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[9][1]
            },
            {
                name:data[10][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[10][1]
            },
            {
                name:data[11][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[11][1]
            },
            {
                name:data[12][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[12][1]
            },
            {
                name:data[13][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[13][1]
            },
            {
                name:data[14][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[14][1]
            },
            {
                name:data[15][0],
                type:'bar',
                stack: '总量',
                itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
                data:data[15][1]
            }
        ]
    };
    myCharts.setOption(option)
})

// 词云图
$.get('http://127.0.0.1:5000/task3').done(function (data) {
    var myCharts = echarts.init(document.querySelector('.right-bottom .charts'));
    option = {
            tooltip: {},
            series: [{
                type: 'wordCloud',
                gridSize: 2,
                sizeRange: [12, 50],
                textRotation:[0, 45, 90, -45],
                shape: 'pentagon',
                width: '100%',
                height: '85%',
                drawOutOfBound: true,
                textStyle: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 255),
                            Math.round(Math.random() * 255),
                            Math.round(Math.random() * 255)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    textStyle: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                },
                data:data
            }]
}
    myCharts.setOption(option)
})

// 售完房价条形图
$.get('http://127.0.0.1:5000/task4').done(function (data) {
    var myCharts = echarts.init(document.querySelector('.right-top .charts'));
    option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
            }
        },
        grid: {
            top: '7%',
            right: '1%',
            left: '14%',
            bottom: '15%'
        },
        xAxis: [{
            type: 'category',
            data: data.name,
            axisLine: {
                lineStyle: {
                    color: 'rgba(255,255,255,0.12)'
                }
            },
            axisLabel: {
                margin: 10,
                color: '#e2e8ff',
                textStyle: {
                    fontSize: 11,
                },
                interval: 0,
                rotate: 30,
            },
        }],
        yAxis: [{
            axisLine: {
                show: false,
                lineStyle: {
                    color: 'rgba(255,255,255,1)'
                },
                splitLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,0.5)'
                    }
                }
            },
        }],
        series: [{
            type: 'bar',
            data: data.value,
            itemStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0,244,255,1'
                    },
                    {
                        offset: 1,
                        color: 'rgba(0,77,167,1'
                    }
                    ]),
                    barBorderRadius: [30, 30, 30, 30],
                    shadowColor: 'rgba(0,160,221,1',
                    shadowBlur: 4,
                }
            }
        }]
    }
        myCharts.setOption(option)
})

// 在售房价条形图
$.get('http://127.0.0.1:5000/task5').done(function (data) {
    var myCharts = echarts.init(document.querySelector('.right-center .charts'));
    option = {
      tooltip: {
          trigger: 'axis',
          axisPointer: {
              type: 'shadow',
          }
      },
      grid: {
          top: '7%',
          right: '1%',
          left: '14%',
          bottom: '15%'
      },
      xAxis: [{
          type: 'category',
          data: data.name,
          axisLine: {
              lineStyle: {
                  color: 'rgba(255,255,255,0.12)'
              }
          },
          axisLabel: {
              margin: 10,
              color: '#e2e8ff',
              textStyle: {
                  fontSize: 11,
              },
              interval: 0,
              rotate: 30,
          },
      }],
      yAxis: [{
          axisLine: {
              show: false,
              lineStyle: {
                  color: 'rgba(255,255,255,1)'
              },
              splitLine: {
                  lineStyle: {
                      color: 'rgba(255,255,255,0.5)'
                  }
              }
          },
      }],
      series: [{
          type: 'bar',
          data: data.value,
          itemStyle: {
              normal: {
                  color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                      offset: 0,
                      color: 'rgba(0,244,255,1'
                  },
                  {
                      offset: 1,
                      color: 'rgba(0,77,167,1'
                  }
                  ]),
                  barBorderRadius: [30, 30, 30, 30],
                  shadowColor: 'rgba(0,160,221,1',
                  shadowBlur: 4,
              }
          }
      }]
  }
        myCharts.setOption(option)
})

// 待售房价条形图
$.get('http://127.0.0.1:5000/task6').done(function (data) {
    var myCharts = echarts.init(document.querySelector('.top-bottom .charts'));
    option = {
          tooltip: {},
      legend: {
        show: false,
      },
      grid: {
        top: '1%',
        left: '-15%',
        right: '15%',
        bottom: '1%',
        containLabel: true
      },
      xAxis: {
        type: "value",
        splitLine: {
          show: false,
        },
        axisLabel: {
          show: false,
        },
        axisTick: {
          show: false,
        },
        axisLine: {
          show: false,
        },
      },
      yAxis: [
        {
          type: "category",
          inverse: true,
          axisLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisPointer: {
            label: {
              show: false,
              margin: 30,
            },
          },
          data: data.name,
          axisLabel: {
            margin: 70,
            fontSize: 14,
            align: "left",
            color: "rgba(255,255,255,0.85)",
            // 配置序号背景
            rich: {
              a1: {
                color: "#FFD743",
                width: 30,
                height: 30,
                align: "center",
              },
              a2: {
                color: "#4690FF",
                width: 30,
                height: 30,
                align: "center",
              },
              a3: {
                color: "#FF8A45",
                width: 30,
                height: 30,
                align: "center",
              },
              b: {
                color: "rgba(255,255,255,0.65)",
                width: 30,
                height: 30,
                align: "center",
              },
            },
            formatter: function (params, index) {
              var leftIndex = index + 1;
              if (leftIndex < 4) {
                return ["{a" + leftIndex + "|" + leftIndex + "}" + "  "+params].join(
                  "\n"
                );
              } else {
                return ["{b|" + leftIndex + "}" + "  " +params].join("\n");
              }
            },
          },
        },
      ],
      series: [
        {
          zlevel: 2,
          type: "bar",
          barWidth: 12,
          data: data.value,
          itemStyle: {
            color: {
              type: "linear",
              x: 0,
              y: 0,
              x2: 1,
              y2: 0,
              colorStops: [
                {
                  offset: 0,
                  color: "rgba(27,46,204,0.9)", // 0% 处的颜色
                },
                {
                  offset: 1,
                  color: " #41D7FF", // 100% 处的颜色
                },
              ],
            },
            barBorderRadius: [8, 8, 8, 8],
          },
          label: {
            show: true,
            position: "right",
            color: "rgba(255,255,255,2)",
            fontSize: 14,
            offset: [10, 1],
            formatter:function(params){
              return params.value
            }
          },
        },
      ],
    }
        myCharts.setOption(option)
})

// 玫瑰图
$.get('http://127.0.0.1:5000/task7').done(function (data) {
var myCharts = echarts.init(document.querySelector('.left-bottom .charts'));
    option = {
            tooltip: {
                trigger: 'item',
                formatter: '{b} : {c}套 ({d}%)'
            },
            grid: {
            top: '1%',
            left: '1%',
            right: '%',
            bottom: '1%',
            },
            legend: {
                top: 'bottom',
                textStyle:{ color: 'white' }
            },
            series: [{
                type: 'pie',
                radius: ['20%', '60%'],
                center: ['50%', '50%'],
                roseType: 'area',
                itemStyle: { borderRadius: 8 },
                data: data.data
        }]
        }
    myCharts.setOption(option)
})