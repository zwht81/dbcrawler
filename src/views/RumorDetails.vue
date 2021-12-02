<template>
  <div class="root">
  <!-- <div style="margin:0; padding:0;background:linear-gradient(to right, #bb313e25, #bb313e25, #d7222925, #dd4a1625, #e4761525, #f5c50025, #f0e92725, #b1ce2425, #48a93525, #03944525, #157c4f25, #176a5825, #1b556325, #1d386f25, #1d386f25, #20277825, #52266325, #8a244b25);"> -->
    <span class="title">
      <b>Covid</b> Rumor
    </span>
    <el-divider/>
    <div style="display: flex; flex-direction:column; justify-content: center; align-items: center;">
      <div class="text_title">{{title}}</div>

      <div>
        <span style="color:grey;">共</span>
        <b style="color:#FFB74D;">{{content.length}}</b>
        <span style="color:grey;">字，预计需要</span>
        <b style="color:#FFB74D;">{{minutes}}</b>
        <span style="color:grey;">分钟阅读</span>
      </div>
        
      <div class="text_item">{{content}}</div>
    
    </div>
  </div>
</template>

<script>
import api from '../commonApi.js'
export default {
  name: "RumorDetails",
  components: {

  },
  data() {
    return {
        title:null,
        content:null,
        createtime:null,
        load:0
    };
  },
  computed: {
    minutes () {
      return Math.floor(this.content.length / 200)
    }
  },
  mounted : function(){
        var _this = this;
        let formData = new FormData();
        formData.append('rumor_id', this.$route.params.id);
        this.$axios
        .post(api.baseApi+'/notice/rumor_detail',formData)
        .then(function(response) {
            console.log(response.data)
            if (response.data.success) {  
                  _this.title=response.data.data.rumor_title
                  _this.content=response.data.data.rumor_content
                  _this.createtime=response.data.data.rumor_created_time
                // console.log(_this.posts) 
          }else {
            this.$message({message: response.data.message,
                    type: 'error'})
          }
        })
    }

}
</script>
<style scoped>
.root {
  margin-top: 100px;
  display:flex;
  justify-content:center;
  align-items:center;
  flex-direction: column;
}
.title {
    font-size:80px; 
    align-self: flex-start; 
    position: relative;
    left: 250px;
  }
.text_title {
  /* outline: #00ff00 dotted thick;  */
  font-size:37px;
  font-weight:700;
  width: 1000px;
  margin-top: 20px;
  margin-bottom: 10px;
}
.text_item {
  /* outline: #00ff00 dotted thick;  */
  margin-top: 50px;
  margin-bottom: 20px;
  
  width: 80%;
  font-size: 20px;
  line-height: 1.8;
  letter-spacing: 1.5px;

  padding: 20px;

  border-radius: 20px;
	
	box-shadow: 0px 0px 20px 4px rgba(128, 128, 128, 0.1);
}
</style>
