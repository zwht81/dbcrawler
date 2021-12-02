<template>
    <div class="travelRoot">
        <airline-detail/>

        <div class="track" style="padding:20px;margin:0 auto;margin-top:10px;">
            <h1 style="font-size:20px;margin-bottom:18px;">
                疫情轨迹
            </h1>

            <div class="trackCardRoot" style='margin-bottom: 20px;'>
                <div class="row">
                    <div class="trackCity">印度尼西亚</div>
                    <track-card destination="浙江杭州"></track-card>
                    <track-card destination="浙江徐州"></track-card>
                </div>
                <div>2021/06/23-2021/07/07</div>
            </div>
            <div class="trackCardRoot">
                <div class="row">
                    <div class="trackCity">广州东莞</div>
                    <track-card destination="陕西咸阳"></track-card>
                    <track-card destination="紫阳县汉王镇"></track-card>
                </div>
                <div>2021/07/02-2021/07/09</div>
            </div>
        </div>

    </div>
</template>
<script>
    // import SelectBar from '../components/common/SelectBar.vue'
    // import TravelCard from '../components/common/TravelCard.vue'
    // import TravelTable from '../components/charts/TravelTable.vue'
    import TrackCard from '@/components/common/TrackCard.vue'
    import AirlineDetail from "../components/AirlineDetail";

    export default {
        name: "Travel",
        components: {
            AirlineDetail,
            // SelectBar,
            // TravelCard,
            // TravelTable,
            TrackCard,
        },
        data() {
            return {
                SearchInput: '',
                buttons: ['国内', '国际'],
                showChina: true,
                track: [
                    [
                        {position: '浙江杭州', coordinate: "120.21201,30.2084"},
                        {position: '浙江徐州', coordinate: "117.18554,34.28823"},
                    ],
                    [
                        {position: '广东东莞', coordinate: "113.75179,23.02067"},
                        {position: '陕西咸阳', coordinate: "108.70641,34.32908"},
                        {position: '紫阳县汉王镇', coordinate: "108.446617,32.714622"},

                    ],
                    []

                ]
            }
        },
        methods: {
            selected(index, differkey) {
                if (differkey == '国内') {
                    switch (index) {
                        case 0:
                            this.showChina = true
                            break
                        case 1:
                            this.showChina = false
                            break
                    }
                }
            },
        }
    }
</script>
<style scoped>

    .travelRoot {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .travelTitle {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 70px;

        position: relative;
        right: 400px;
    }

    .titleText {
        font-size: 30px;
        align-self: flex-start;
        position: relative;

    }

    .travelTitle .SelectBar {
        /* outline: #00ff00 dotted thick; */

        margin-left: 30px;
    }


    .travelMain {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .travelUpSection {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .travelMap {
        /* background-color: rgb(0, 0, 0); */
        justify-content: center;
        align-items: center;
        text-align: center;
        width: 800px;
        height: 650px;
        margin: 30px;

        border: #cccccc solid thin;
        border-radius: 40px;
    }

    .travelDownSection {
        margin-top: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .travelTable {
        margin-left: 20px;
        width: 550px;
    }

    .track {
        border: #cccccc solid thin;
        border-radius: 40px;
        width: 80%;
        justify-content: center;
        align-items: center;
    }

    .trackCardRoot {
        border: #bfbec0 solid thin;
        border-radius: 30px;
        width: auto;
        height: 80px;

        position: relative;

        display: flex;
        /* flex-direction: column; */
        align-items: center;
        justify-content: space-around;
        white-space: nowrap;
    }

    .trackCity {
        font-size: 40px;
        font-weight: bold;

        white-space: nowrap;
        text-align: center;

        font-size: 27px;
        font-weight: 500;

        background-color: #e6e6e6;

        border-radius: 30px;

        padding: 5px 15px 5px 15px;
        margin: 3px;

    }

    .row {
        display: flex;
        margin-right: 0px;
        flex-direction: row;
    }
</style>
