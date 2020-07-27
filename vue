<template>
    <div class="reportGeneratePage">
        <Row type="flex" style="margin-top: 20px">
            <Col span="2" order="1"></Col>
            <Col span="20" order="2">
                <Row type="flex">
                    <Col span="12" order="1" style="text-align: left">
                        <Select style="width: 120px;margin-left: 20px" v-model="selectedType" filterable clearable
                                placeholder="请选择手机型号">
                            <Option style="text-align:left" v-for="type in typeList" :value="type.typeName"
                                    :key="type.typeUuid">{{ type.typeName }}
                            </Option>
                        </Select>
                    </Col>
                    <Col span="12" order="2" style="text-align: right">
                        <Badge :count="selectedSequences.length" style="margin-right: 20px">
                            <Icon type="ios-folder-outline" size="28" @click="showSelectedSequences=true"/>
                            <a href="#" class="demo-badge"></a>
                        </Badge>
                    </Col>
                </Row>
                <Row style="margin-top: 20px">
                    <Table :columns="t_sequences" :data="sequenceList">
                        <template slot-scope="{ row, index }" slot="operation">
                            <Button type="primary" size="small" @click="viewSequence(row)">添加序列</Button>
                        </template>
                    </Table>
                </Row>
                <Row style="margin-top: 20px">
                    <Page :total="total" size="small" show-elevator show-sizer />
                </Row>
                <br>
                <hr>
                <br>
                <Row style="text-align: right">
                    <Button type="primary" size="small" @click="generateReport" style="margin-right: 20px">生成报告</Button>
                </Row>
            </Col>
            <Col span="2" order="3"></Col>
        </Row>

        <Modal v-model="showSelectedSequences" width="80%" title="下面是已选择的序列">
            <Table :columns="t_sequences" :data="selectedSequences">
                <template slot-scope="{ row, index }" slot="operation">
                    <Button type="error" size="small" @click="removeSelectedSequence(row)"
                            style="margin-left: 10px;margin-right: 10px">取消选择
                    </Button>
                    <Button type="primary" size="small" style="margin-right: 5px" @click="viewSequence(row)">查看场景</Button>
                </template>
            </Table>
        </Modal>

        <Modal v-model="showSequenceDetail" width="80%" title="请选择场景" @on-ok="addSequence()" :styles="{top:'20px'}">
            <Scroll height="600">
                <Card :bordered="true" v-for="testChip in selectedSequence.testChips"
                      style="margin-bottom:10px">
                    <Row>
                        <Col span="11">
                            测试场景:<span>{{testChip.testChipName}}</span>
                        </Col>
                        <Col span="11">
                            手机设置:<span>{{testChip.phoneMode}}</span>
                        </Col>
                        <Col span="2">
                            <Checkbox v-model="testChip.selected">选中</Checkbox>
                        </Col>
                    </Row>
                    <br>
                    <Row>
                        <Col span="8" style="text-align: center">
                            <img src="http://pic.netbian.com/uploads/allimg/190518/174718-15581728388724.jpg"
                                 width="120" height="90">
                        </Col>
                        <Col span="8" style="text-align: center">
                            <img src="http://pic.netbian.com/uploads/allimg/190518/174718-15581728388724.jpg"
                                 width="120" height="90">
                        </Col>
                        <Col span="8" style="text-align: center">
                            <img src="http://pic.netbian.com/uploads/allimg/190518/174718-15581728388724.jpg"
                                 width="120" height="90">
                        </Col>
                    </Row>
                </Card>
            </Scroll>
        </Modal>
    </div>
</template>

<script>
    export default {
        name: 'reportGeneratePage',
        data() {
            return {
                typeList: [],
                selectedType: {typeName:"huawei",typeUuid:"-1"},
                selectedSequence: '',
                showSelectedSequences: false,
                showSequenceDetail: false,
                selectedSequences: [],
                sequenceList: [],
                total: 40,
                pageCurrent: 1,
                pageSize: 10,
                t_sequences: [
                    {title: '测试序列', key: 'sequenceName'},
                    {title: '测试实例', key: 'testcaseName'},
                    {title: '样机型号', key: 'phoneType'},
                    {title: '样机模式', key: 'phoneMode'},
                    {title: '测试时间', key: 'testTime'},
                    {title: '测试人员', key: 'tester'},
                    {title: '操作', slot: 'operation', width: 200}
                ]
            }
        },


        methods: {
            getSequenceList: function () {
                var url = "http://localhost:8093/sequence/getSequenceList"
                var data = qs.


                this.sequenceList = [
                    {
                        sequenceUuid: "123123",
                        sequenceName: "123123",
                        testcaseName: "默认X10",
                        phoneType: "ELS",
                        phoneMode: "默认长焦",
                        testTime: "2020-7-26",
                        tester: "william",
                        testChips: [
                            {
                                sceneName: "KTV",
                                selected: true,
                                picIds: [
                                    "123", "223", "323"
                                ]
                            }
                        ]
                    },
                    {
                        sequenceUuid: "223123",
                        sequenceName: "223123",
                        testcaseName: "默认X10",
                        phoneType: "ELS",
                        phoneMode: "默认长焦",
                        testTime: "2020-7-26",
                        tester: "william",
                        testChips: [
                            {
                                sceneName: "KTV",
                                selected: true,
                                picIds: [
                                    "123", "223", "323"
                                ]
                            }
                        ]
                    },
                    {
                        sequenceUuid: "323123",
                        sequenceName: "323123",
                        testcaseName: "默认X10",
                        phoneType: "ELS",
                        phoneMode: "默认长焦",
                        testTime: "2020-7-26",
                        tester: "william",
                        testChips: [
                            {
                                sceneName: "KTV",
                                selected: true,
                                picIds: [
                                    "123", "223", "323"
                                ]
                            }
                        ]
                    }
                ]
            },

            getTypeList: function () {
                this.typeList = [
                    {typeName: "ELS", typeUuid: "123456"},
                    {typeName: "ELS-NEW", typeUuid: "223456"},
                    {typeName: "ANNA", typeUuid: "323456"},
                    {typeName: "ANNA-NEW", typeUuid: "423456"},
                    {typeName: "NOP", typeUuid: "523456"},
                    {typeName: "NOH", typeUuid: "623456"}
                ]
            },

            viewSequence: function (sequence) {
                this.selectedSequence = sequence
                this.showSequenceDetail = true
                for (var i in this.selectedSequences){
                    if (this.selectedSequences[i].sequenceUuid==sequence.sequenceUuid){
                        this.selectedSequence = this.selectedSequences[i]
                    }
                }
                this.selectedSequence = sequence
            },
            addSequence: function () {
                for (var i in this.selectedSequences){
                    if (this.selectedSequence.sequenceUuid == this.selectedSequences[i].sequenceUuid){
                        this.selectedSequences[i] = this.selectedSequence
                        this.selectedSequence = ""
                        return
                    }
                }
                this.selectedSequences.push(this.selectedSequence)
            },

            removeSelectedSequence: function (sequence) {
                for (var i in this.selectedSequences){
                    if(this.selectedSequences[i].sequenceUuid==sequence.sequenceUuid){
                        this.selectedSequences.splice(i,1)
                    }
                }
            }
        },

        created() {
            this.getTypeList()
            this.getSequenceList()
        }

    }
</script>
