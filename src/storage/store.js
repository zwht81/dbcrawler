import createPersistedState from 'vuex-persistedstate'
import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
	userState: {
		isLogined: false,
		id: '',
		name: '',
		type: '',
		affiliation: '',
		show_sub: false,
	}
  },
  mutations: {
	login (state, userInfo) {
		state.userState.isLogined = true
		state.userState.name = userInfo.name
		state.userState.id = userInfo.id
		state.userState.type = userInfo.type
		state.userState.affiliation = userInfo.affiliation 
		state.userState.show_sub = userInfo.show_sub
	},
	reset (state) {
		state.userState.isLogined = false
		state.userState.name = ''
		state.userState.id = ''
		state.userState.type = ''
		state.userState.affiliation = ''
		state.userState.show_sub = false
	},
	haveRead (state) {
		state.userState.show_sub = false
	},
  },
  getters: {
	userState: state => {
		return state.userState
	}
  },
  plugins: [createPersistedState()]
})

export default {
	store,
}