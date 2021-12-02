import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/travel',
    name: 'travel',
    component: () => import('../views/Travel.vue')
  },
  {
	path: '/login',
	name: 'Login',
	component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/news',
    name: 'News',
    component: () => import('../views/News.vue')
   },
   {
	path: '/test',
	name: 'Test',
	component: () => import('../views/Test.vue')
	},
  {
  path: '/news/:id',
  name: 'NewsDetails',
  component: () => import('../views/NewsDetails.vue')
  },
  {
    path: '/rumor/:id',
    name: 'RumorDetails',
    component: () => import('../views/RumorDetails.vue')
  },
  {
  path: '/notice/:id',
  name: 'NoticeDetails',
  component: () => import('../views/NoticeDetails.vue')
  },
  {
    path: '/question',
    name: 'Question_All',
    component: () => import('../views/QuestionAll.vue')
  },
  {
    path: '/knowledge',
    name: 'Knowledge',
    component: () => import('../views/Knowledge.vue')
  },
  {
    path: '/question/:id',
    name: 'Question',
    component: () => import('../views/Question.vue')
  },
  {
    path: '/knowledge/:id',
    name: 'Knowledge',
    component: () => import('../views/Question.vue')
  },
  {
    path: '/subscribe',
    name: 'Subscribe',
    component: () => import('../views/Subscribe.vue')
  },
  {
    path:'/chinaanalysis',
    name:'ChinaAnalysis',
    component: () => import('../views/ChinaAnalysis.vue')
  },
  {
    path:'/globalanalysis',
    name:'GlobalAnalysis',
    component: () => import('../views/GlobalAnalysis.vue')
  },
  {
    path: '/policy',
    name: 'PolicyAI',
    component: () => import('../views/PolicyAI.vue')
  },
  {
    path: '/forecast',
    name: 'Forecast',
    component: () => import('../views/Forecast.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
