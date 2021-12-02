<template>
  <div >
    <div id="BingChart" style="width: 1000px; height: 540px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
var CountryTrans = require("../../data/utils/countries.json");
var option;
export default{
    name: 'BingChart',
    props: {
        dataType:{
            type: String,
            require: true
        },
        dataTable:{
            type: Array,
            require: true
        }
    },
    data() {
        return {
            myChart:"",
        };
    },
    created() {

    },
    mounted() {
        this.myChart = echarts.init(document.getElementById('BingChart'));
        this.getData();
    },
    methods: {
        getData(){
            this.mycharts()
        },
        mycharts(){
            //console.log("Hello from Other Side",this.$props.dataTable[0])
            var PresentData = this.$props.dataTable[0]
            var SaveList = [];
            var All = PresentData["overview"][this.$props.dataType]["nownum"];
            var Sum = 0;
            //console.log("Test",PresentData["detailed"][0][this.$props.dataType])
            var SortData = PresentData["detailed"]
            var _this = this;
            SortData.sort(function(a,b){
                return (b[_this.$props.dataType]-a[_this.$props.dataType]);
            });
            //console.log(All)

            var Count = SortData.length;
            if (Count>10) {
                Count = 10;
            }
            for (var i=0;i<Count;i++)
            {
                //console.log("项目展示",i,SortData[i]["name"],SortData[i][this.$props.dataType]);
                var CountryName = SortData[i]["name"];
                for (var j=0;j<CountryTrans.length;j++)
                {
                    if (CountryTrans[j]["value"]==CountryName)
                    {
                        CountryName = CountryTrans[j]["label"];
                        break;
                    }
                }
                //console.log("countryname:",CountryName);
                Sum += SortData[i][this.$props.dataType];
                SaveList.push({value:SortData[i][this.$props.dataType],name:CountryName})
            }
            SaveList.push({value:(Math.abs(All-Sum)),name:"其他"})
            //console.log(SaveList);
            option = {
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                //minShowLabelAngle: 2,
                series: [
                    {
                        name: '访问来源',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '40',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: SaveList
                    }
                ]
            };
            this.myChart.setOption(option)
        },
    },
    watch: {
        dataType(){
            this.getData()
        },
        dataTable(){
            this.getData()
        }
    }
};
</script>
<style scoped>

</style>
