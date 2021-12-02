<template>
    <div>
        <span class="timeshow">{{timeString}}</span>
    </div>
</template>
<script>
export default({
    name:"TimeShow",
    props:{
        time:{
            type:String,
            required:true
        }
    },
    computed:{
        timeString(){// 转化时间格式
            return this.$props.time;
        }
    }
})
</script>
<style>
.timeshow {
    color: rgb(184, 184, 184);
    font-family: "Gill Sans", sans-serif;
    font-size: 13px;
    font-weight: 500;
}
</style>
