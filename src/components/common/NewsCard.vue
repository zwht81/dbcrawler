<template>
  <v-card
    class="mx-auto"
    width="344"
  >
    <v-img
      src='../../assets/backgroundImage/news0.png'
      height="80px"
      v-if="showImage.a"
    ></v-img>

    <v-img
      src='../../assets/backgroundImage/news1.png'
      height="80px"
      v-if="showImage.b"
    ></v-img>

    <v-img
      src='../../assets/backgroundImage/news2.png'
      height="80px"
      v-if="showImage.c"
    ></v-img>

    <v-card-title>
      {{title | cutLongTitle}}
    </v-card-title>

    <v-card-subtitle style="display: flex">
      Latest Covid News
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        :color="this.color"
        text
        @click="goToNewsPage()"
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          {{content | cutLongText}}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>


<script>
export default {
    name:'NewsCard',
    data () {
        return {
            show: false,
            color: "orange lighten-2",
        }
    },
    computed: {
      showImage () {
        return {
          a: (this.title.length % 7) == 0,
          b: (this.title.length % 7) == 1,
          c: (this.title.length % 7) == 2
        }
      },
    },
    props: ['title', 'link', 'content'],
    methods: {
      goToNewsPage() {
        this.$router.push(this.link)
      },
    },
    filters: {
      cutLongText: function (value) {
        let maxLenth = 200
        if (value.length > maxLenth) {
          return value.slice(0, maxLenth) + '...'
        }
        return value
      },
      cutLongTitle: function (value) {
        let maxLenth = 50
        if (value.length > maxLenth) {
          return value.slice(0, maxLenth) + '...'
        }
        return value
      }
    },
}
</script>
