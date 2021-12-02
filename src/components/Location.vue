<template>
    <div>
        <div class="locationHeader">
            <div class="region">{{ locationDescription }}</div>
            <div style="display: flex; align-items: center">
              <span
                style="font-size: 20px; margin-left: 10px; margin-right: 5px; color: #444444;"
                >
                <i class="el-icon-location"></i>
                当前位置
              </span>
             
            </div>
        </div>

        <div class="locationOverview">
              <LittleDataCard
                :nownum="cases"
                :newnum="newcases"
                type="累计确诊"
                color="#AC3500"
              />

               <LittleDataCard
                :nownum="deaths"
                :newnum="newdeaths"
                type="累计死亡"
                color="black"
              />

               <LittleDataCard
                :nownum="recovered"
                :newnum="newrecovered"
                type="累计治愈"
                color="#00ACA5"
              />

               <!-- <LittleDataCard
                :nownum="city.vaccine"
                :newnum="city.newvaccine"
                type="疫苗"
                color="#00ACA5"
              /> -->
          </div>

    </div>
</template>

<script>
import LittleDataCard from "./common/LittleDataCard"
import api from '../commonApi.js'
export default {
    name: 'Location',
    components: {
        LittleDataCard,
    },
    mounted () {
      this.getData()
      this.getLocation()
    },
    data() {
      return {
        // locationInfo: {
        //   ip: '',
        //   country: '',
        //   province: '',
        //   city: '',
        //   district: '',
        //   location: '',
        // },
        locationInfo: {
          ip: '',
          country: '中国',
          province: '北京市',
          city: '北京市',
          district: '海淀区',
          location: '116.310316,39.956074',
        },
        // locationInfo: {
        //   ip: '',
        //   country: '中国',
        //   province: '香港特别行政区',
        //   city: '',
        //   district: '',
        //   location: '116.310316,39.956074',
        // },
        // locationInfo: {
        // 	ip: '',
        // 	country: '美国',
        // 	province: '',
        // 	city: '',
        // 	district: '',
        // 	location: '116.310316,39.956074',
        // },
        cases: 0,
        deaths: 0,
        newcases: 0,
        newdeaths: 0,
        newrecovered: 0,
        newvaccine: 0,
        nowcases: 0,
        recovered: 0,
        vaccine: 0,
      };
    },
    computed: {
        locationDescription () {
            if (this.locationInfo.country == '中国') {
                if (this.locationInfo.province == this.locationInfo.city) {
                    return this.locationInfo.city + this.locationInfo.district
                } else {
                    return this.locationInfo.province + this.locationInfo.city + this.locationInfo.district
                }
            } else {
                return this.locationInfo.country
            }
        },
    },
    methods: {
        getLocation () {
            // eslint-disable-next-line
          this.locationInfo.ip = returnCitySN.cip

          var _this = this
          this.$axios.get("https://restapi.amap.com/v5/ip?key=a593d64ab73229be6b3d1ef802b76849&type=4&ip="+this.locationInfo.ip)
            .then( response => {
              _this.locationInfo.country = response.data.country
              _this.locationInfo.province = response.data.province
              _this.locationInfo.city = response.data.city
              _this.locationInfo.district = response.data.district
              _this.locationInfo.location = response.data.location

              console.log(_this.locationInfo)
              _this.getData()
            })
        },
        getData () {
          let formData = new FormData();
          formData.append('ip', this.locationInfo.ip);
          formData.append('country', this.locationInfo.country);
          formData.append('province', this.locationInfo.province);
          formData.append('city', this.locationInfo.city);
          formData.append('district', this.locationInfo.district);
          formData.append('location', this.locationInfo.location);

          let _this = this
          this.$axios
          .post(api.baseApi+'/data/current_location_data',formData)
          .then(response => {
            console.log(response)

            _this.cases = response.data.data.cases
            _this.deaths = response.data.data.deaths
            _this.newcases = response.data.data.newcases
            _this.newdeaths = response.data.data.newdeaths
            _this.newrecovered = response.data.data.newrecovered
            _this.newvaccine = response.data.data.newvaccine
            _this.nowcases = response.data.data.nowcases
            _this.recovered = response.data.data.recovered
            _this.vaccine = response.data.data.vaccine
          })

        }
    },
}

</script>

<style scoped>
.locationHeader {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  margin-bottom: 20px;

  align-self: start;
}
.region {
  white-space: nowrap;
  text-align: center;

  font-size: 27px;
  /* font-weight: 500; */

  background-color: #e0e0e0;
  color: rgb(105, 105, 105);

  /* border: #cccccc solid 2px; */
  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin: 3px;
}

.locationOverview { 
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding-left: 25px;
  padding-right: 25px;
  padding-top: 5px;
  padding-bottom: 5px;
  border: #cccccc solid thin;
  border-radius: 10px;

  width: 500px;
}
</style>