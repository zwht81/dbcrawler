<template>
    <div class="s_table_root">
        <v-app>
            <v-card class="s_table">
                <v-card-title>
                    <v-text-field
                            v-model="search"
                            append-icon="mdi-magnify"
                            label="Search"
                            single-line
                            hide-details
                            color="#00ACA5"
                    ></v-text-field>
                </v-card-title>
                <v-data-table
                        :headers="headers"
                        :items="detailed"
                        :search="search"
                        :custom-filter="customFilter"
                        :footer-props="{
            disableItemsPerPage: true,
            itemsPerPageOptions: [10],
          }"
                        color="#00ACA5"
                >
                    <!--          <template v-slot:[`item.nowcases`]="{ item }">-->
                    <!--            <v-chip :color="getColor(item.nowcases)" dark>-->
                    <!--              {{ item.nowcases }}-->
                    <!--            </v-chip>-->
                    <!--          </template>-->
                </v-data-table>
            </v-card>
        </v-app>
    </div>
</template>

<script>
    // var countryen2zh = require('../../data/utils/countryen2zh.json')
    // var provinceen2zh = require('../../data/utils/china_en2province.json')
    export default {
        name: 'AirlineTable',
        props: {
            province: {
                type: String,
                required: true
            },
            tableData: {
                type: Array,
                required: true
            }
        },
        watch: {
            tableData() {
                this.loadData();
            }
        },
        mounted() {
            this.loadData();
        },

        data() {
            return {
                search: '',
                headers: [
                    {
                        text: '未选择',
                        align: 'start',
                        sortable: false,
                        value: 'name',
                    },
                    {
                        text: '已计划',
                        value: 'schesum',
                    },
                    {
                        text: '已取消',
                        value: 'cancel',
                    },
                    {
                        text: '已执行',
                        value: 'execsum',
                    },
                    {
                        text: '历史同期执行',
                        value: 'execsumHis',
                    },

                    // { text: '现有确诊', value: 'nowcases' },
                    // { text: '累积确诊', value: 'cases' },
                    // { text: '累积治愈', value: 'recovered' },
                    // { text: '累积死亡', value: 'deaths' },
                    // { text: '疫苗接种', value: 'vaccine' },
                ],
                detailed: [],
            }
        },
        methods: {
            // getColor (nowcases) {
            //   if (nowcases > 100000) return 'red'
            //   else if (nowcases > 1000) return 'orange'
            //   else return 'green'
            // },
            customFilter(_, search, item) {
                if (item.name.toLowerCase().search(search.toLowerCase()) !== -1) return true;
                return false;
            },
            loadData() {
                // console.log(this.detailed);
                this.detailed = this.$props.tableData;
                this.headers[0].text = this.$props.province;
                // var i;
                // var item;
                // if(this.$props.type ==="China"){
                //   this.headers[0].text = "省份";
                //   for(i in this.detailed){
                //     for(item in provinceen2zh){
                //       if(provinceen2zh[item]["value"] === this.detailed[i]["name"]){
                //         this.detailed[i]["zhname"] = provinceen2zh[item]["label"];
                //         break;
                //       }
                //     }
                //   }
                // } else{
                //   this.headers[0].text = "国家";
                //   for(i in this.detailed){
                //     for(item in countryen2zh){
                //       if(countryen2zh[item]["value"] == this.detailed[i]["name"]){
                //         this.detailed[i]["zhname"] = countryen2zh[item]["label"];
                //         break;
                //       }
                //     }
                //   }
                // }
            }
        }
    }
</script>

<style>
    .s_table_root {
        padding: 10px;
        height: 670px;
        overflow: hidden;
    }

    .s_table th {
        font-size: 18px !important;
        white-space: nowrap !important;
    }

    .s_table td {
        font-size: 18px !important;
    }
</style>