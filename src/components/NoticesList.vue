<template>
<v-app >
    <h1>{{title}}</h1>
    <p style="color:grey;">共{{total}}条通告</p>
    <!-- <div
        style="margin: 30px"
        v-for="post in posts.slice((this.currentPage - 1) * this.eachPage,
            this.currentPage * this.eachPage)"
        v-bind:key="post.notice_id"
    >
        <NewsCard v-bind:title="post.notice_title" :link="'notice/'+post.notice_id" :content="post.notice_content"/>
    </div> -->
    <v-timeline >
    <v-timeline-item
      v-for="(post) in posts.slice(0,
            this.a)"
      :key="post.notice_title"
      color="red lighten-1"
      small
    >
      <template v-slot:opposite>
       <span
          :class="`headline font-weight-bold --text`"
          v-text="post.notice_created_time.slice(0,10)"
        ></span>
      </template>
      <div class="py-1">
        <h2 :class="`headline font-weight-light mb-1 --text`">
          <div v-text="post.notice_title"  :link="'notice/'+post.notice_id"  @click="goToNewsPage('notice/'+post.notice_id)"> </div>
        </h2>
        <div>
         <div v-if="post.notice_created_time.slice(0,10) === '2021-07-14' " class="con" v-text="post.notice_content.slice(11)" :link="'notice/'+post.notice_id"></div>
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
    <!-- <v-pagination
        style="margin-top: 30px;"
        v-model="currentPage"
        :length="Math.ceil(total / eachPage)"
        circle
        color="orange lighten-2"
    ></v-pagination> -->
     <div class="load-more mr-bottom" v-if="a<total"  @click='loadMore' >点击加载更多</div>
 <div class="load-more mr-bottom" v-else >没有更多了</div>
</v-app>
</template>


<script>
import api from '../commonApi.js'
// import NewsCard from './common/NewsCard.vue'

export default {
    name:"NoticesList",
    data(){
        return {
            a:14,
            posts: [
            //      {news_id:"1",news_title: '关于印发新型冠状病毒肺炎诊疗方案（试行第八版 修订版）的通知',news_content: "新闻内容01",news_created_time: "2021-07-04T10:53:50Z"} ,
            //      {news_id:"2",news_title: '关于调整《新冠肺炎疫情相关租金减让会计处理规定》适用范围的通知',news_content: "新闻内容01",news_created_time: "2021-07-04T10:53:50Z"} ,
            ],
            years: [
        {
          color: 'cyan',
          year: '1960',
        },
            ],
            // currentPage: 1,
            // eachPage: 5,
            total: 0,
            page:1,
            page_count:''
        }
    },
    props: ['title'],
    components: {
        // NewsCard
    },    
    methods:{
         loadMore:function(){
          this.a+=5
        },
        goToNewsPage(link) {
        this.$router.push(link)
        },
        fetchData () {
        let _this = this
        this.$axios
            .get(api.baseApi+'/notice/list_all_notice')
            .then(function(response) {
                // console.log(response.data)
                if (response.data.success) {  
                    for ( var m in response.data.data){
                        _this.posts.push(response.data.data[m])
                        // console.log(response.data.data)
                    }
                    // console.log(_this.posts)
                    _this.total = _this.posts.length 
                }else {
                    this.$message({message: response.data.message,
                                    type: 'error'})
                }
            })
        }
    },
    mounted : function(){
        this.fetchData ()
    },
}
</script>

<style scoped>
.con{
    overflow: hidden;
    text-overflow:ellipsis;
    display:-webkit-box;
    -webkit-box-orient:vertical;
    -webkit-line-clamp:3;
}
</style>