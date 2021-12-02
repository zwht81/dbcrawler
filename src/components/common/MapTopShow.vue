<template>
<div class="root">
    <div v-for="item in types" :key="item.id">
        <map-top-show-card :type="typeName(item)" :nownum="calnownum(item)" :newnum="calnewnum(item)" ></map-top-show-card>
    </div>
</div>
</template>
<script>
import MapTopShowCard from "./MapTopShowCard.vue"
export default ({
    name:"MapTopShow",
    props:{
        data:{
            type:Object,
            required:true
        }
    },
    data(){
        return {
            types:["cases","deaths","recovered","vaccine"],
            mapping:{
                cases:"确诊",
                deaths:"死亡",
                recovered:"治愈",
                vaccine:"疫苗"
            }
        }
    },
    components:{
        MapTopShowCard
    },
    methods:{
        calnownum(type){
            var res=0;
            for(var i in this.$props.data[type][0]){
                res += this.$props.data[type][0][i]["value"];
            }
            return res;
        },
        calnewnum(type){
            if(this.$props.data[type].length==1)return this.calnownum(type);
            var res=0;
            for(var i in this.$props.data[type][0]){
                res += this.$props.data[type][1][i]["value"];
            }
            return this.calnownum(type)-res;
        },
        typeName(type){
            return this.mapping[type];
        }
    }
})
</script>
<style scoped>
.root {
    /* outline: #00ff00 dotted thick; */

    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;

    width: 400px;
}
</style>