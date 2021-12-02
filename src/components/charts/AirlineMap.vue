<template>
    <div id="airline-map-root">

        <span class="travelTitle" >
		<span class='titleText'>
			<b>Covid</b> <span>Travel</span>
		</span>
		<SelectBar class='SelectBar' :buttons="buttons1"/>
		</span>
		<el-divider/>

        <div style='display: flex; align-items: flex-start; justify-content: center;'>
            <v-app>
                <v-card class="route-table">
                    <v-card-title>
                        <v-text-field
                                v-model="departActual"
                                label="出发地"
                                single-line
                                hide-details
                                color="#00ACA5"
                        ></v-text-field>
                        →
                        <v-text-field
                                v-model="arriveActual"
                                label="到达地"
                                single-line
                                hide-details
                                color="#00ACA5"
                        ></v-text-field>
                        <el-button style="font-size: 18px; font-weight: bold; margin: 20px; cursor: pointer;" round
                                    @click="updateRoute">查询
                        </el-button>
                    </v-card-title>

                    <v-card-text>
                        <v-text-field label="筛选航班号" v-model="search"></v-text-field>
                        <div v-if="showRouteType===0" class="route-list">
                            <div v-for="(item, index) in currFlights_show"
                                    v-bind:key="index">
                                <div @click="showFlightRouteDetail(item)" style="cursor: pointer;">
                                    <TravelCard class='route-list-card'
                                            :key="item.flight_number"
                                            :startTime='item.departure_date'
                                            :arriveTime='item.arrival_date'
                                            :start='item.departure_city_name'
                                            :destination='item.arrival_city_name'
                                            :num='item.flight_number'
                                            :status='item.state'/>
                                </div>
                            </div>
                        </div>
                        <div v-else-if="showRouteType===1" class="route-list">
                            <div v-for="(item, index) in currTrains_show"
                                    v-bind:key="index">
                                <div @click="showTrainRouteDetail(item)" style="cursor: pointer;">
                                    <TravelCard class='route-list-card'
                                            :key="item.train_id"
                                            :startTime='item.departure_time'
                                            :arriveTime='item.arrival_time'
                                            :start='item.departure_city'
                                            :destination='item.arrival_city'
                                            :num='item.train_id'
                                            :status="item.aaa"/>
                                </div>
                            </div>
                        </div>
                    </v-card-text>
                </v-card>
            </v-app>

            <div style=' margin-left: 30px;'>

                <v-card
                class="mx-auto"
                color="rgb(230, 162, 60)"
                dark
                max-width="700px"
                >

                    <v-card-title>
                        <v-icon
                        large
                        left
                        >
                        mdi-bell
                        </v-icon>
                        <span class="text-h6 font-weight-light">行程信息</span>
                    </v-card-title>

                    <v-card-text style='font-weight: bold; font-size: 20px;' v-if="doShowRouteDetail">


                        <h3 style="margin-bottom: 15px;">{{departCity}} → {{arriveCity}}
                            <span v-if="vehicleType === 0" style='margin-left:25px;'>交通工具:飞机</span>
                            <span v-else-if="vehicleType === 1" style='margin-left:25px;'>交通工具:列车</span>
                            <span style='margin-left:25px;'>班次:{{currId}}</span>
                        </h3>

                        <b v-if="warnMessage===0">行程<span style="color: green">不接近</span>中高风险及其附近地区，无较大风险，请依然全程正确佩戴口罩，远离人群，做好必要防护措施！</b>
                        <b v-if="warnMessage===1">行程<span style="color: darkred">途经</span>中高风险及其附近地区，有轻微风险，请注意全程正确佩戴口罩，远离人群，做好必要防护措施！</b>
                        <b v-if="warnMessage===2">行程<span style="color: darkred">目的地</span>为中高风险及其附近地区，有较大风险，若无紧急事件建议酌情取消或暂缓行程，建议出发前提前接种疫苗，行程过程中以及到达目的地后请做好必要防护措施，谨防疫情传播！</b>
                        <b v-if="warnMessage===3">行程<span style="color: darkred">出发地</span>为中高风险及其附近地区，有较大风险，若无紧急事件建议酌情取消或暂缓行程，出发前请务必检查是否持有核酸检测及疫苗接种证明，行程过程中以及到达目的地后请做好必要防护措施，主动隔离，谨防疫情传播！</b>

                    </v-card-text>

                    <v-card-text v-else style='font-weight: bold; font-size: 20px;'>
                        点击左侧搜索到的班次以显示详细信息
                    </v-card-text>

                </v-card>

                <div id="airline-map"></div>

            </div>
        </div>

    </div>
</template>

<script>
    import * as echarts from "echarts";
    // import AirlineTable from "./AirlineTable";
    import SelectBar from "../common/SelectBar";
    import api from "../../commonApi";
    import $ from "jquery";
    import TravelCard from "../common/TravelCard";

    var mapData;
    var data = [];
    var mainCityList = [];

    export default {
        name: "AirlineMap",
        components: {
            TravelCard,
            // AirlineTable,
            SelectBar
        },
        computed: {
            currFlights_show () {
                return this.currFlights.filter(
                item => item.flight_number.indexOf(this.search)>=0
                )
            },
            currTrains_show() {
                return this.currTrains.filter(
                item => item.train_id.indexOf(this.search)>=0
                )
            }
        },
        created() {
            var risk_data;
            $.ajax({
                url: api.baseApi + "/data/list_all_high_risk_areas",
                type: 'GET',
                async: false,
                dataType: 'json',
                success: function (response) {
                    risk_data = response.data;
                    // console.log(risk_data);
                }

            });
            this.risk_data = risk_data;
            // this.risk_data.push({type: '中风险', province: '江苏省', district: '南京市\n(测试用）', name: '', coordinate: []});
            // console.log(this.risk_data);
            this.risk_data.forEach((item) => {
                var currCoord;
                $.ajax({
                    url: api.baseApi + '/travel/find_center_city_coordinate',
                    type: 'POST',
                    async: false,
                    dataType: 'json',
                    data: {
                        name: item.district.slice(0, 2),
                    },
                    success: function (response) {
                        currCoord = [parseFloat(response.data.longitude), parseFloat(response.data.latitude)]
                    }
                });
                if (item.type === "中风险") {
                    this.option.series[3].data.push({
                        name: item.district,
                        value: currCoord,
                    });
                } else if (item.type === "高风险") {
                    this.option.series[4].data.push({
                        name: item.district,
                        value: currCoord,
                    });
                }
                // console.log(this.option.series[4].data);
                // console.log(this.high_risk);
            });
            // console.log(this.option.series[3].data);
            // console.log(this.option.series[4].data);
        },
        mounted() {
            require('echarts/lib/component/geo');
            this.myChart = echarts.init(document.getElementById("airline-map"));
            // require("echarts/lib/component/geo");
            this.myChart.showLoading();
            this.loadMap();
            // console.log(mapData);
            mapData.features.forEach((item) => {
                var properties = item.properties;
                data.push(properties);
            });
            var _this = this;
            this.myChart.on("click", function (param) {
                _this.clickevent(param);
            });
            // $.ajax({
            //     url: "https://www.umetrip.com/gateway/api/web/umeflightstatus-live/live/getchartstatistics",
            //     type: 'POST',
            //     async: false,
            //     dataType: 'json',
            //     data: {},
            //     success: function (response) {
            //         // console.log(response);
            //         chartData = response
            //     }
            // });
            // console.log(chartData);
            // arrCivil = chartData.arrCivil;
            // depCivil = chartData.depCivil;
            // var coords = [
            //     this.departCoord,
            //     this.arriveCoord
            // ];
            // this.setCoords([
            //     coords
            // ])
            $.ajax({
                url: api.baseApi + '/travel/list_all_main_cities',
                type: 'GET',
                async: false,
                dataType: 'json',
                data: {},
                success: function (response) {
                    mainCityList = response.data;
                }
            });
        },
        data() {
            return {
                myChart: "",
                mapName: "China",
                curr: "",
                buttons: ["入境", "出境"],
                buttons1: ["航班", "列车"],
                switchContent: 0,
                showRouteType: 0,       //0显示航班，1显示列车
                tableData: [],
                departActual: "",
                arriveActual: "",
                departCity: "",
                departCoord: [],
                arriveCity: "",
                arriveCoord: [],
                currFlights: [],
                currTrains: [],
                risk_data: [],
                vehicleType: 0,
                search: '',
                flag: false,
                currId: "",
                warnMessage: 0,
                rawWarnMessage: 0,
                doShowRouteDetail: false,
                option: {
                    // title: {
                    //     text: "行程显示",
                    // },
                    // visualMap: {
                    // left: 'right',
                    // textStyle: {
                    //     color: "#000",
                    // },
                    // pieces: [
                    //     {min: 0, max: 0,label:'低风险',color:'#EAE0D7'},
                    //     {min: 1, max: 1,label:'中风险',color:'#f46d43'},
                    //     {min: 2, max: 2,label:'高风险',color:'#a50026'},
                    // ],
                    // },
                    geo: [{
                        map: 'China',
                        itemStyle: {
                            color: "#000"
                        },
                        zoom: 1.5,
                        center: [103.71878, 36.10396],
                    }],
                    series: [
                        {                       //index: 0
                            name: "",
                            coordinateSystem: 'geo',
                            nameProperty: "name",
                            zoom: 1.5,
                            center: [103.71878, 36.10396],
                            type: "map",
                            map: "",
                            roam: false,
                            data: [],
                            normal: {
                                label: {
                                    show: true,
                                },
                            },
                            emphasis: {
                                label: {
                                    show: true
                                }
                            },
                            itemStyle: {
                                normal: {
                                    label: {
                                        show: true,
                                        textStyle: {
                                            color: "rgb(144 144 144)",
                                        },
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                    }
                                }
                            }
                        },
                        {                       //index: 1
                            name: "directPath",
                            coordinateSystem: 'geo',
                            type: 'lines',
                            // polyline: true,
                            // effect: {
                            //     show: true,
                            //     trailWidth: 1,
                            //     trailOpacity: 0.5,
                            //     trailLength: 0.2,
                            //     constantSpeed: 5
                            // },

                            // blendMode: 'lighter',

                            lineStyle: {
                                color: '#555555',
                                width: 3,
                                opacity: 1,
                                curvness: 0.2,
                                type: [5, 10],
                                dashOffset: 5
                            },
                            zlevel: 5,
                            data: []
                        },
                        {                          //index: 2
                            name: "trainPath",
                            coordinateSystem: 'geo',
                            type: 'lines',
                            polyline: true,
                            lineStyle: {
                                color: '#555555',
                                width: 3,
                                opacity: 1,
                                type: [5, 10],
                                dashOffset: 5
                            },
                            zlevel: 5,
                            data: []
                        },
                        {                           //index: 3
                            name: 'midRiskArea',
                            type: "scatter",
                            symbol: 'pin',
                            coordinateSystem: 'geo',
                            data: [],
                            symbolSize: 75,
                            zlevel: 10,
                            label: {
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9
                                }
                            },
                            itemStyle: {
                                // 标志颜色
                                normal: {
                                    color: '#aaa331',
                                    label: {
                                        show: true,
                                        color: '#fff',
                                        fontSize: 15,
                                        formatter: function () {
                                            // console.log(param);
                                            return "中风险";
                                        }
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        zlevel: 20,
                                        formatter: function (param) {
                                            // console.log(param);
                                            return param.name;
                                        }
                                    },
                                },
                            }
                        },
                        {                               //index: 4
                            name: 'highRiskArea',
                            type: "scatter",
                            symbol: 'pin',
                            coordinateSystem: 'geo',
                            data: [],
                            symbolSize: 100,
                            zlevel: 10,
                            label: {
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9
                                }
                            },
                            itemStyle: {
                                // 标志颜色
                                normal: {
                                    color: '#F62157',
                                    label: {
                                        show: true,
                                        fontSize: 18,
                                        formatter: function () {
                                            // console.log(param);
                                            return "高风险";
                                        }
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        zlevel: 20,
                                        formatter: function (param) {
                                            // console.log(param);
                                            return param.name;
                                        }
                                    },
                                },
                            }
                        },
                        {                           //index: 5
                            name: 'departCity',
                            type: "scatter",
                            symbol: 'pin',
                            coordinateSystem: 'geo',
                            data: [],
                            symbolSize: 100,
                            zlevel: 10,
                            label: {
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9
                                }
                            },
                            itemStyle: {
                                // 标志颜色
                                normal: {
                                    color: '#32a3ff',
                                    label: {
                                        show: true,
                                        fontSize: 18,
                                        color: '#fff',
                                        formatter: function () {
                                            // console.log(param);
                                            return "起始地";
                                        }
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        zlevel: 20,
                                        formatter: function (param) {
                                            // console.log(param);
                                            return param.name;
                                        }
                                    },
                                },
                            }
                        },
                        {                           //index: 6
                            name: 'arriveCity',
                            type: "scatter",
                            symbol: 'pin',
                            coordinateSystem: 'geo',
                            data: [],
                            symbolSize: 100,
                            zlevel: 10,
                            label: {
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9
                                }
                            },
                            itemStyle: {
                                // 标志颜色
                                normal: {
                                    color: '#ff7800',
                                    label: {
                                        show: true,
                                        fontSize: 18,
                                        color: '#fff',
                                        formatter: function () {
                                            // console.log(param);
                                            return "目的地";
                                        }
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        zlevel: 20,
                                        formatter: function (param) {
                                            // console.log(param);
                                            return param.name;
                                        }
                                    },
                                },
                            }
                        },
                        {                           //index: 7
                            name: 'passCities',
                            type: "scatter",
                            symbol: 'pin',
                            coordinateSystem: 'geo',
                            data: [],
                            symbolSize: 50,
                            zlevel: 10,
                            label: {
                                show: true,
                                textStyle: {
                                    color: '#fff',
                                    fontSize: 9
                                }
                            },
                            itemStyle: {
                                // 标志颜色
                                normal: {
                                    color: '#b422b4',
                                    label: {
                                        show: true,
                                        fontSize: 12,
                                        color: '#fff',
                                        formatter: function () {
                                            // console.log(param);
                                            return "";
                                        }
                                    },
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        zlevel: 20,
                                        formatter: function (param) {
                                            // console.log(param);
                                            return param.name;
                                        }
                                    },
                                },
                            }
                        }
                    ]
                },

            }
        },
        watch: {
            // mapName() {
            //     this.loadMap();
            // },
            // curr() {
            //
            //     var currContent = [];
            //     var _this = this;
            //     if (this.switchContent === 0) {
            //         currContent = arrCivil.find(function (item) {
            //             return item.provinceName === _this.curr;
            //         });
            //
            //     } else if (this.switchContent === 1) {
            //         currContent = depCivil.find(function (item) {
            //             return item.provinceName === _this.curr;
            //         });
            //     }
            //     // console.log(currContent);
            //     this.tableData = [];
            //     this.tableData.push(currContent.now);
            //     this.tableData[0].name = "总计";
            //     this.tableData[0].execsumHis = currContent.execsumHis;
            //     currContent.airportInfoList.forEach(function (item) {
            //         _this.tableData.push(item.now);
            //         _this.tableData[_this.tableData.length - 1].name = item.airportName;
            //         _this.tableData[_this.tableData.length - 1].execsumHis = item.execsumHis;
            //     });
            // },
            // switchContent() {
            //     var currContent;
            //     var _this = this;
            //     if (this.switchContent === 0) {
            //         currContent = arrCivil.find(function (item) {
            //             return item.provinceName === _this.curr;
            //         });
            //
            //     } else if (this.switchContent === 1) {
            //         currContent = depCivil.find(function (item) {
            //             return item.provinceName === _this.curr;
            //         });
            //     }
            //     // console.log(currContent);
            //     this.tableData = [];
            //     this.tableData.push(currContent.now);
            //     this.tableData[0].name = "总计";
            //     this.tableData[0].execsumHis = currContent.execsumHis;
            //     currContent.airportInfoList.forEach(function (item) {
            //         _this.tableData.push(item.now);
            //         _this.tableData[_this.tableData.length - 1].name = item.airportName;
            //         _this.tableData[_this.tableData.length - 1].execsumHis = item.execsumHis;
            //     });
            // },
            showRouteType() {
                // console.log(this.showRouteType)
            },
            departCity() {
                // console.log(this.getProvinceByCity(this.departCity));
                var _this = this;
                $.ajax({
                    url: api.baseApi + '/travel/find_center_city_coordinate',
                    type: 'POST',
                    async: false,
                    dataType: 'json',
                    data: {
                        name: _this.departCity,
                    },
                    success: function (response) {
                        _this.departCoord = [parseFloat(response.data.longitude), parseFloat(response.data.latitude)]
                    }
                });
                this.importFilghtsTrains();
                this.option.series[1].data = [];
                this.option.series[2].data = [];
                this.option.series[5].data = [{name: this.departCity, value: this.departCoord}];
                this.option.series[7].data = [];
                this.warnMessage = 0;
                this.myChart.setOption(this.option);
                var departProvince = this.getProvinceByCity(this.departCity);
                var arriveProvince = this.getProvinceByCity(this.arriveCity);
                if (this.risk_data.findIndex(function (item) {
                    return item.province.search(departProvince) >= 0;
                }) >= 0) this.warnMessage = 3;
                else if(this.risk_data.findIndex(function (item) {
                    return item.province.search(arriveProvince) >= 0;
                }) >= 0) this.warnMessage = 2;
                this.rawWarnMessage = this.warnMessage;
                this.doShowRouteDetail = false;
            },
            arriveCity() {
                // console.log(this.getProvinceByCity(this.arriveCity));
                var _this = this;
                $.ajax({
                    url: api.baseApi + '/travel/find_center_city_coordinate',
                    type: 'POST',
                    async: false,
                    dataType: 'json',
                    data: {
                        name: _this.arriveCity,
                    },
                    success: function (response) {
                        _this.arriveCoord = [parseFloat(response.data.longitude), parseFloat(response.data.latitude)]
                    }
                });
                this.importFilghtsTrains();
                // console.log(this.arriveCoord);
                this.option.series[1].data = [];
                this.option.series[2].data = [];
                this.option.series[6].data = [{name: this.arriveCity, value: this.arriveCoord}];
                this.option.series[7].data = [];
                this.warnMessage = 0;
                this.myChart.setOption(this.option);
                var departProvince = this.getProvinceByCity(this.departCity);
                var arriveProvince = this.getProvinceByCity(this.arriveCity);
                if (this.risk_data.findIndex(function (item) {
                    return item.province.search(departProvince) >= 0;
                }) >= 0) this.warnMessage = 3;
                else if(this.risk_data.findIndex(function (item) {
                    return item.province.search(arriveProvince) >= 0;
                }) >= 0) this.warnMessage = 2;
                this.rawWarnMessage = this.warnMessage;
                this.doShowRouteDetail = false;
            },
            flag() {
                this.myChart.setOption(this.option);
            }
        },
        methods: {
            loadMap() {
                mapData = require("../../data/map/json/GeoMapData_CN/" + this.mapName);
                echarts.registerMap("China", mapData);
                this.option["series"][0]["name"] = this.mapName;
                this.option["series"][0]["map"] = this.mapName;
                this.myChart.setOption(this.option);
                this.myChart.hideLoading();
            },
            clickevent(param) {
                this.curr = data.find(function (item) {
                    return item.name === param.name;
                }).shorter;
            },
            // setCoords(data) {
            //     if (data !== undefined) {
            //         this.option["series"][1].data = data;
            //         // this.myChart.setOption(this.option);
            //         // this.myChart.hideLoading();
            //     } else {
            //         this.option["series"][1].data = [];
            //         // this.myChart.setOption(this.option);
            //         // this.myChart.hideLoading();
            //     }
            // },
            // setTrainPath(data) {
            //
            // },
            selected(index, differkey) {
                if (differkey === "入境") {
                    this.switchContent = index;
                } else if (differkey === "航班") {
                    this.showRouteType = index;
                }
            },
            updateRoute() {
                if (this.arriveActual === "" || this.departActual === "") alert("输入不能为空！");
                else {
                    this.departCity = this.departActual;
                    this.arriveCity = this.arriveActual;
                    this.departActual = "";
                    this.arriveActual = "";
                }
            },
            importFilghtsTrains() {
                var _this = this;
                $.ajax({
                    url: api.baseApi + '/travel/find_specific_flight_info',
                    type: 'POST',
                    async: false,
                    dataType: 'json',
                    data: {
                        departure_city: _this.departCity,
                        arrival_city: _this.arriveCity,
                    },
                    success: function (response) {
                        _this.currFlights = response.data
                    }
                });
                // var coords = [
                //     this.departCoord,
                //     this.arriveCoord
                // ];
                // this.setCoords([
                //     coords
                // ]);
                $.ajax({
                    url: api.baseApi + '/travel/find_specific_train_info',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        departure_city: _this.departCity,
                        arrival_city: _this.arriveCity,
                    },
                    success: function (response) {
                        _this.currTrains = response.data
                    }
                });
            },
            showFlightRouteDetail(data) {
                // console.log(data);
                this.doShowRouteDetail = true;
                //清空轨迹和途经
                this.option.series[2].data = [];
                this.option.series[7].data = [];
                this.option.series[1].data = [[this.departCoord, this.arriveCoord]];
                // this.myChart.setOption(this.option)
                this.flag = !this.flag;
                this.warnMessage = this.rawWarnMessage;
                this.vehicleType = 0;
                this.currId = data.flight_number;
            },
            showTrainRouteDetail(data) {
                // console.log(data);
                this.doShowRouteDetail = true;
                //清空轨迹和途经
                this.option.series[1].data = [];
                this.option.series[2].data = [[this.departCoord]];
                this.option.series[7].data = [];
                this.warnMessage = this.rawWarnMessage;
                var stations = data.pass_city.split(',');
                var _this = this;
                var startIdx = stations.findIndex(function (item) {
                    return item.search(_this.departCity) >= 0;
                });
                var endIdx = stations.findIndex(function (item) {
                    return item.search(_this.arriveCity) >= 0;
                });
                // console.log(startIdx);
                // console.log(endIdx)
                stations = stations.slice(startIdx + 1, endIdx - startIdx);
                // console.log(stations)
                stations.forEach((item) => {
                    $.ajax({
                        url: api.baseApi + '/travel/find_center_city_coordinate',
                        type: 'POST',
                        async: false,
                        dataType: 'json',
                        data: {
                            name: item,
                        },
                        success: function (response) {
                            var tempCoord = [parseFloat(response.data.longitude), parseFloat(response.data.latitude)];
                            _this.option.series[2].data[0].push(tempCoord);
                            _this.option.series[7].data.push({name: item, value: tempCoord});
                        }
                    });
                });
                this.option.series[2].data[0].push(this.arriveCoord);
                this.flag = !this.flag;
                this.vehicleType = 1;
                this.currId = data.train_id;
                if(this.warnMessage === 0) {
                    stations.forEach((item) => {
                        if (_this.risk_data.findIndex(function (item1) {
                            return item1.province.search(_this.getProvinceByCity(item)) >= 0;
                        }) >= 0) {
                            _this.warnMessage = 1;
                        }
                    });
                }
            },
            getProvinceByCity(city) {
                var res =  mainCityList.find(function (item) {
                    return item.city.search(city) >= 0;
                });
                if (res !== undefined)
                    return res.province;
                else return "unfetchable";
            }
        }
    }

</script>

<style scoped>
    .route-table {
        width: 600px;
        height: 800px;
        overflow: scroll;
    }
    .route-list-card {
        margin: 15px;
    }

    .travelTitle {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 70px;

        position: relative;
        right: 400px;
    }

    .titleText {
        font-size: 30px;
        align-self: flex-start;
        position: relative;

    }

    .travelTitle .SelectBar {
        /* outline: #00ff00 dotted thick; */

        margin-left: 30px;
    }

    #airline-map {
        border: #cccccc solid thin;
        border-radius: 10px;
        overflow: hidden;
        
        width: 700px; 
        height: 600px;

        margin-top: 35px;
    }
</style>