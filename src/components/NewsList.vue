<template>
<v-app >

    <h1>{{title}}</h1>
    <p style="color:grey;">共{{this.posts_show.length}}条新闻</p>

    <center>
        <el-input
          placeholder="Search"
          v-model="search"
          style="width: 70%; margin-bottom: 10px;"
          >
          <i slot="prefix" class="el-input__icon el-icon-search"></i>
        </el-input>
    </center>

    <div
        style="margin: 30px"
        v-for="post in posts_show.slice((this.currentPage - 1) * this.eachPage,
            this.currentPage * this.eachPage)"
        v-bind:key="post.news_id"
    >
        <NewsCard v-bind:title="post.news_title" :link="'news/'+post.news_id" :content="post.news_content"/>
    </div>
    <v-pagination
        style="margin-top: 30px;"
        v-model="currentPage"
        :length="Math.ceil(this.posts_show.length / eachPage)"
        circle
        color="orange lighten-2"
    ></v-pagination>

</v-app>
</template>


<script>
import api from '../commonApi.js'
import NewsCard from './common/NewsCard.vue'

export default {
    name:"NewsList",
    data(){
        return {
            posts: [],
            currentPage: 1,
            eachPage: 5,
            search: '',
        }
    },
    props: ['title'],
    computed: {
        posts_show () {
            return this.posts.filter(
                item => item.news_title.indexOf(this.search)>=0
            )
        }
    },
    components: {
        NewsCard
    },    
    methods:{
        fetchData () {
        let _this = this
        this.$axios
            .get(api.baseApi+'/news/list_all_news')
            .then(function(response) {
                // console.log(response.data)
                if (response.data.success) {  
                    for ( var m in response.data.data){
                        _this.posts.push(response.data.data[m])
                        // console.log(response.data.data)
                    }
                    // console.log(_this.posts)
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

</style>