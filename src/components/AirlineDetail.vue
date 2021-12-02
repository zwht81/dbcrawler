<template>
    <div class="AirlineDetailRoot">

        <airline-map ref="AirlineMap">
        </airline-map>
<!--        <el-button style="font-size: 18px; font-weight: bold; margin: 20px;" round>国内预警航线</el-button>-->
<!--        <div class="TravelWarningList">-->
<!--            <TravelCard v-for="item in risk_flights"-->
<!--                        :key="item.flight_number"-->
<!--                        :startTime='item.departure_date'-->
<!--                        :arriveTime='item.arrival_date'-->
<!--                        :start='item.departure_city_name'-->
<!--                        :destination='item.arrival_city_name'-->
<!--                        :num='item.flight_number'-->
<!--                        :status='item.status'/>-->
<!--        </div>-->
    </div>
</template>

<script>
    import AirlineMap from "./charts/AirlineMap";
    // import api from "../commonApi.js";
    // import $ from "jquery";
    // import TravelCard from "./common/TravelCard";

    export default {
        name: "AirlineDetail",
        components: {AirlineMap},
        // data() {
        //     return {
        //
        //     }
        // }
        data() {
            return {
                risk_flights: [],
                risk_area: [
                    {
                        province: '云南',
                        city: '德宏',
                        level: 'high'
                    }
                ],
            }
        },
        created() {

        }
    }
</script>

<style scoped>

</style>