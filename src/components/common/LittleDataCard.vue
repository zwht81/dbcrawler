<template>
    <div class="showcardroot">
        <div class="nownum"><span :style="'color:'+this.color">{{nowanimatednum | cutLongNum}}</span></div>
        <div class="type">{{type}}</div>
        <div class="newnum"> 较上日 <span class="newNumVal" :style="'color:' + this.color">  {{newanimatednum | cutLongNewNum}} </span> </div>
    </div>
</template>
<script>
import gsap from "gsap/gsap-core"

export default({
    name:"LittleDataCard",
    props: ['nownum', 'type', 'newnum', 'color'],
    data(){
        return{
            newnumber:0,
            nownumber:0,
        }

    },
    mounted(){
        this.newnumber = this.$props.newnum;
        this.nownumber = this.$props.nownum;
    },
    filters: {
        cutLongNum (value) {

            if ( value > 1000000) {
                return (value/1000000).toFixed(1) + 'M'
            } else if ( value > 1000) {
                return (value/1000).toFixed(1) + 'k'
            }
            return value
        },
        cutLongNewNum (value) {

            var sign = "+"
            if (value < 0) {
                sign = "-"
                value = -value
            }

            if ( value > 1000000) {
                return sign + (value/1000000).toFixed(1) + 'M'
            } else if ( value > 1000) {
                return sign + (value/1000).toFixed(1) + 'k'
            }
            return sign+value
        },
    },
    computed:{
        nowanimatednum:function(){
            if(typeof(nownumber) == undefined)return 0;
            return this.nownumber.toFixed(0);
        },
        newanimatednum:function(){
            if(typeof(newnumber) == undefined)return 0;
            return this.newnumber.toFixed(0);
        }

    },
    watch:{
        nownum:function(newvalue){
            gsap.to(this.$data,{duration:0.5,nownumber:newvalue})
        },
        newnum:function(newvalue){
            gsap.to(this.$data,{duration:0.5,newnumber:newvalue})
        }
    }
})

</script>

<style scoped>
.showcardroot {
    margin: 10px;
    margin-left:15px;
    margin-right:15px;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;

    white-space: nowrap;
}
.nownum {
    font-family: "Gill Sans", sans-serif;
    font-size: 30px;
    font-weight: 600;
}
.newnum {
    color: rgb(104, 105, 106);
    font-size: 14px;
    font-weight: 500;
    display: flex;
    align-items: center;
}
.newNumVal {
	color: #000000;
    font-size: 22px;
	font-weight: 900;
}
.type {
  white-space: nowrap;
  text-align: center;

  font-size: 16px;
  font-weight: 500;

  background-color:rgba(20, 20, 20, 0.3);
  color: white;

  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin: 3px;
}
</style>
