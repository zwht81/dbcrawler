<template>
    <div class="showcardroot">
        <div class="nownum">{{nownum}}</div>
        <div class="type">{{type}}</div>
        <div class="newnum">新增 +{{newnum}}</div>
    </div>
</template>
<script>
export default({
    name:"MapTopShowCard",
    props:{
        nownum:{
            type:Number,
            required:true
        },
        type:{
            type:String,
            required:true
        },
        newnum:{
            type:Number,
            required:true
        }
    }
})
</script>

<style scoped>
.showcardroot {
    margin: 10px;
    margin-left:15px; 
    margin-right:15px;
}
.nownum {
    color: white;
    font-family: "Gill Sans", sans-serif;
    font-size: 25px;
    font-weight: 600;
}
.newnum {
    color: rgb(184, 184, 184);
    font-family: "Gill Sans", sans-serif;
    font-size: 13px;
    font-weight: 100;
}
.type {
  white-space: nowrap;
  text-align: center;

  font-size: 15px;
  font-weight: 100;

  background-color:rgba(20, 20, 20, 0.2);
  color: white;

  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin: 3px;
}
</style>
