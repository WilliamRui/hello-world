<template>
    <div class="page">
        <div class="Rhead">
            <!--下拉框-->
            <div class="selector">
                <div class="dropdown">
                    <a class="btn btn-secondary btn-sm dropdown-toggle" href="#" role="button" id="dropdownMenuLink"
                       data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{selectedType}}
                    </a>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                        <a class="dropdown-item" href="#" v-for="type in types" v-on:click="filter(type)">{{type}}</a>
                    </div>
                </div>
            </div>
            <!--计数器-->
            <div class="counter">
                <button type="button" class="btn btn-primary btn-sm" data-toggle="modal"
                        data-target="#selectedSequences">
                    已选择 <span class="badge badge-light">{{count}}</span>
                </button>
            </div>
        </div>

        <div class="Rbody">
            <div class="title row">
                <div class="col-md-2">
                    <span>测试用例</span>
                </div>
                <div class="col-md-2">
                    <span>手机型号</span>
                </div>
                <div class="col-md-2">
                    <span>相机模式</span>
                </div>
                <div class="col-md-2">
                    <span>测试时间</span>
                </div>
                <div class="col-md-2">
                    <span>测试人员</span>
                </div>
                <div class="col-md-2">
                    <span>操作</span>
                </div>
            </div>
            <div class="data row" v-for="sequence in sequences">
                <div class="col-md-2">
                    <span>{{sequence.name}}</span>
                </div>
                <div class="col-md-2">
                    <span>{{sequence.type}}</span>
                </div>
                <div class="col-md-2">
                    <span>{{sequence.mode}}</span>
                </div>
                <div class="col-md-2">
                    <span>{{sequence.time}}</span>
                </div>
                <div class="col-md-2">
                    <span>{{sequence.tester}}</span>
                </div>
                <div class="col-md-2">
                    <input type="button" value="选择图片" data-toggle="modal" data-target="#sequenceDetail"
                           v-on:click="sendId(sequence.id)">
                </div>
            </div>
            <div class="Rpagination row">
                <div class="col-md-12">
                    <nav aria-label="Page navigation example">
                        <ul class="pagination pagination-sm justify-content-end">
                            <li class="page-item disabled">
                                <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                            </li>
                            <li class="page-item"><a class="page-link" href="#">1</a></li>
                            <li class="page-item"><a class="page-link" href="#">2</a></li>
                            <li class="page-item"><a class="page-link" href="#">3</a></li>
                            <li class="page-item">
                                <a class="page-link" href="#">Next</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>

        <div class="Rfooter">
            <button class="btn btn-primary btn-sm btn-submit" type="submit">提交</button>
        </div>

        <!-- Modal1 -->
        <div class="modal fade" id="sequenceDetail" data-backdrop="static" data-keyboard="false" tabindex="-1"
             role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-header">
                        <h6 class="modal-title" id="staticBackdropLabel">请选择场景</h6>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>

                    <div class="modal-body">
                        <div class="scene" v-for="scene in scenes">
                            <div class="scene-info">
                                <label>场景名称：<span>{{scene.name}}</span></label>
                                <label>相机模式：<span>{{scene.mode}}</span></label>
                            </div>
                            <div class="scene-pic">
                                <img src="https://tse2-mm.cn.bing.net/th/id/OIP.7uCkVcryBNI29E9C73wMSAHaEZ?w=275&h=180&c=7&o=5&dpr=1.5&pid=1.7">
                                <img src="https://tse2-mm.cn.bing.net/th/id/OIP.7uCkVcryBNI29E9C73wMSAHaEZ?w=275&h=180&c=7&o=5&dpr=1.5&pid=1.7">
                                <img src="https://tse2-mm.cn.bing.net/th/id/OIP.7uCkVcryBNI29E9C73wMSAHaEZ?w=275&h=180&c=7&o=5&dpr=1.5&pid=1.7">
                            </div>
                        </div>
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm" data-dismiss="modal">取消</button>
                        <button type="button" class="btn btn-primary btn-sm" data-dismiss="modal"
                                v-on:click="selectSequence">确认
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal2 -->
        <div class="modal fade" id="selectedSequences" data-backdrop="static" data-keyboard="false" tabindex="-1"
             role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h6 class="modal-title">已选择测试用例</h6>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="selectedSequence" v-for="selectedSequence in selectedSequences">
                            <div class="selectedSequenceInfo">
                                <label>场景名称：<span>{{selectedSequence.name}}</span></label>
                                <label>相机模式：<span>{{selectedSequence.mode}}</span></label>
                                <label>手机型号：<span>{{selectedSequence.type}}</span></label>
                                <label>测试时间：<span>{{selectedSequence.time}}</span></label>
                                <label>测试人员：<span>{{selectedSequence.tester}}</span></label>
                                <button type="button" class="close" aria-label="关闭"
                                        v-on:click="removeSequence(selectedSequence.id)">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm" data-dismiss="modal">取消</button>
                        <button type="button" class="btn btn-primary btn-sm" data-dismiss="modal">确认
                        </button>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.min.css'
    import 'bootstrap/dist/js/bootstrap.min.js'

    export default {
        name: "page",
        data() {
            return {
                sequences: [
                    {id: 1, name: "测试实例1", type: "手机型号1", mode: "测试模式1", time: "2020-7-22", tester: "william"},
                    {id: 2, name: "测试实例2", type: "手机型号2", mode: "测试模式2", time: "2020-7-22", tester: "william"},
                    {id: 3, name: "测试实例3", type: "手机型号3", mode: "测试模式3", time: "2020-7-22", tester: "william"},
                    {id: 4, name: "测试实例4", type: "手机型号4", mode: "测试模式4", time: "2020-7-22", tester: "william"},
                    {id: 5, name: "测试实例1", type: "手机型号1", mode: "测试模式1", time: "2020-7-22", tester: "william"},
                    {id: 6, name: "测试实例2", type: "手机型号2", mode: "测试模式2", time: "2020-7-22", tester: "william"},
                    {id: 7, name: "测试实例3", type: "手机型号3", mode: "测试模式3", time: "2020-7-22", tester: "william"},
                    {id: 8, name: "测试实例4", type: "手机型号4", mode: "测试模式4", time: "2020-7-22", tester: "william"},
                    {id: 9, name: "测试实例1", type: "手机型号1", mode: "测试模式1", time: "2020-7-22", tester: "william"},
                    {id: 10, name: "测试实例2", type: "手机型号2", mode: "测试模式2", time: "2020-7-22", tester: "william"},
                ],
                scenes: [
                    {name: "KTV", mode: "默认广角"},
                    {name: "办公室", mode: "默认1X"}
                ],
                types: ["手机型号1", "手机型号2", "手机型号3", "手机型号4"],
                count: 0,
                selectedSequences: [],
                tempId: -1,
                filteredSequences: [],
                selectedType: "全部型号"
            }
        },

        methods: {
            selectSequence: function () {
                var id = this.tempId
                for (var i in this.sequences) {
                    var targetId = this.sequences[i].id
                    if (targetId === id) {
                        for (var j in this.selectedSequences) {
                            var selectedId = this.selectedSequences[j].id
                            if (id === selectedId) {
                                return
                            }
                        }
                        this.selectedSequences.push(this.sequences[i])
                        this.count++
                    }
                }
            },
            sendId: function (id) {
                this.tempId = id
                console.log(this.tempId)
            },
            removeSequence: function (id) {
                for (var i in this.selectedSequences) {
                    var targetId = this.selectedSequences[i].id
                    if (id === targetId) {
                        this.selectedSequences.pop(this.selectedSequences[i])
                        this.count--
                    }
                }
            }
        }
    }

</script>

<style>

    /*modal2*/
    .selectedSequence {
        text-align: center;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.3);
    }

    .selectedSequenceInfo label {
        margin-left: 10px;
        margin-right: 10px;
        font-weight: bold;
        font-size: 12px;
    }

    /*modal1*/
    .scene {
        text-align: center;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.3);
    }

    img {
        width: 240px;
        height: 180px;
        margin-left: 10px;
        margin-bottom: 10px;
    }

    .scene-info label {
        margin-left: 100px;
        margin-right: 100px;
        font-weight: bold;
        font-size: 12px;
    }

    h6 {
        font-size: 14px;
        font-weight: bold;
        margin-left: 30px;
    }

    label span {
        font-weight: normal;
    }


    /*Rfooter*/
    .Rfooter {
        margin-top: 10px;
        text-align: right;
    }

    .btn-submit {
        margin-right: 70px;
    }


    /*Rbody*/
    .title {
        margin-top: 10px;
        margin-bottom: 10px;
        font-weight: bold;
        border-bottom: 1px solid black;
        height: 40px;
        line-height: 40px;
        font-size: 12px;
    }

    .data {
        height: 40px;
        line-height: 40px;
        margin-top: 10px;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        font-size: 12px;
        vertical-align: middle;
    }

    .Rpagination {
        border-bottom: 1px solid black;
    }

    input[type='button'] {
        height: 30px;
        margin-top: 5px;
        line-height: 30px;
    }


    .page-item {
        margin-right: 0;
    }


    /*Rhead*/
    .page {
        margin: 20px auto;
        width: 90%;
    }

    .selector a {
        font-size: 14px;
    }

    .selector {
        display: inline-block;
        text-align: left;
        width: 47%;
        margin-left: 40px;
    }

    .counter {
        display: inline-block;
        text-align: right;
        width: 44%;
        margin-right: 20px;
    }


</style>
