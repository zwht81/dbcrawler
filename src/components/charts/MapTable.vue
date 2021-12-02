<template>
  <div id="map-table">
    <el-table class="Mtable" :data="data" height="250" max-height="400px">
      <el-table-column label="区域" width="80"> 
          <template slot-scope = "scope">
              <span @click="clickevent(scope.row)">{{regionName(scope.row.region)}}</span>
          </template>
      </el-table-column>
      <el-table-column label="确诊" width="80"> 
          <template slot-scope = "scope">
              <span @click="clickevent(scope.row)">{{scope.row.cases}}</span>
          </template>
      </el-table-column>
      <el-table-column label="死亡" width="80"> 
          <template slot-scope = "scope">
              <span  @click="clickevent(scope.row)">{{scope.row.deaths}}</span>
          </template>
      </el-table-column>
      <el-table-column label="治愈" width="80"> 
          <template slot-scope = "scope">
              <span @click="clickevent(scope.row)">{{scope.row.recovered}}</span>
          </template>
      </el-table-column>
      <el-table-column label="接种" width="80"> 
          <template slot-scope = "scope">
              <span @click="clickevent(scope.row)">{{scope.row.vaccine}}</span>
          </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
var countrymapping = require("../../data/utils/countryen2zh.json")
export default {
  name: "MapTable",
  props:{
      data:{
          type:Array,
          required:true
      }
  },
  data(){
    return{
      mapping:{}
    } 
  },
  watch:{
    data(){
      this.$props.data.sort(function(a,b){// cases排序，二次迭代添加指定字段排序
      return b.cases-a.cases;
    })
    }
  },
  created(){
    this.mapping = countrymapping;
    this.$props.data.sort(function(a,b){// cases排序，二次迭代添加指定字段排序
      return b.cases-a.cases;
    })
  },
  methods:{
    clickevent(obj){
      this.$parent.changeCountry(obj.region);
    },
    regionName(region){
      for(var i in this.mapping){
        if(this.mapping[i]["value"] == region)return this.mapping[i]["label"];
      }
      return region;
    }
  }
};
</script>

<style>
.Mtable {
  width: 100%; 
  border-radius: 30px; 
  border: #afafaf solid 2px !important;
}
#map-table .el-table th, .el-table tr {
    background-color: rgba(255, 0, 0, 0) !important;
}
#map-table .el-table, .el-table__expanded-cell {
    background-color: #686561 !important;
    color: #d2d2d2 !important;
}
#map-table .el-table thead {
  color: #ffffff !important;
  font-weight: 1000 !important;
  font-size: 16px !important;
}
</style>