<template>
  <div id="nav_bar">
    <div class="nav_bar_frame">
      <div class="nav_bar_icon" @click="backtostartpage">
        <div class="nav_bar_icon_title_bold">Database</div>
        <div class="nav_bar_icon_title"> 数据库</div>
      </div>

      <div class="nav_bar_item_outer_frame">
        <router-link
          :to="item.url"
          tag="div"
          class="nav_bar_item"
          active-class="nav_bar_item_active"
          v-for="item in pages"
          :key="item.name"
        >
          {{ item.title }}
        </router-link>
      </div>
    </div>

    <div
      tag="div"
      class="new_message"
      v-if="show_sub"
      @click="toNewMessage()"
    >
          您的订阅有新的消息 !
    </div>

  </div>
</template>

<script>

export default {
  name: "NavBar",
  components: {
  },
  computed: {
    show_sub () {
      return this.$store.getters.userState.show_sub
    }
  },
  data() {
    return {
      pages: [
        // {
        //   title:"国内疫情",
        //   url:"/chinaanalysis"
        // },
        // {
        //   title:"国际疫情",
        //   url:"/globalanalysis"
        // },
        // {
        //   title:"新闻",
        //   url: "/news",
        // },
        {
          title:"数据",
          url: "/knowledge",
        },
        // {
        //   title:"问答",
        //   url: "/question",
        // },
        // {
        //   title:"行程",
        //   url: "/travel",
        // },
        {
          title:"管理",
          url: "/subscribe",
        }
        // {
        //   title:"预测",
        //   url: "/forecast",
        // },
        // {
        //   title:"关于",
        //   url: "/about",
        // }
      ],
    };
  },
  methods: {
    backtostartpage(){
      this.$router.push('/')
      window.location.reload();
    },
    toNewMessage () {
      this.$store.commit('haveRead')
      this.$router.push('/subscribe')
    },
  }
};
</script>

<style scoped>
.new_message {
  position: absolute; 
  right: 90px; 
  top: 10px; 
  z-index: 12;

  font-weight: bold;
  color: white;

  background-color: rgb(230, 162, 60);
  border-radius: 30px;
  padding: 1px;
  padding-left: 6px;
  padding-right: 6px;

  box-shadow: 0px 0px 10px 2px rgba(128, 128, 128, 0.1);

  cursor: pointer;

}

#user-avatar {
  position: fixed;
  right: 20px;
  top: 3px;
  z-index: 10;
}

#nav_bar {
  position: fixed;
  z-index: 10;
  top: 0px;
  height: 46px;
  width: 100vw;
  vertical-align: middle;

  border: #cecfd2 solid thin;

  backdrop-filter: blur(20px);
  background-color: rgba(255, 255, 255, 0.5);
}
.nav_bar_frame {
  vertical-align: middle;
  height: 45px;
  width: 100%;
}

.nav_bar_icon {
  margin-left: 25px;
  float: left;
  line-height: 45px;
  vertical-align: middle;
  height: 45px;
  cursor: pointer;
}
.nav_bar_icon_title_bold {
  display: inline;
  font-weight: bold;
}
.nav_bar_icon_title {
  display: inline;
}
.nav_bar_item_outer_frame {
  float: left;
  margin-left: 20px;
}
.nav_bar_item {
  display: inline;
  color: black;
  margin: 0px 10px 10px 0px;
  line-height: 45px;
  cursor: pointer;
}
.nav_bar_item_active {
  display: inline;
  line-height: 45px;
  border-bottom-style: outset;
  border-bottom-color: black;
  border-bottom-width: 2px;
  font-weight: bold;
  height: 45px;
  width: 100%;
}
.nav_bar_action_frame {
  float: right;
  margin-right: 50px;
}
.nav_bar_action_link {
  display: inline;
  line-height: 45px;
}
.el-button--text {
  font-size: 16px;
  color: rgb(7, 7, 7);
}
.el-button--text:hover {
  font-size: 16px;
  color: rgb(7, 7, 7);
}

.nav_bar_new_status {
  position: relative;
  right: 100px;
  top: 5px;
}
</style>
