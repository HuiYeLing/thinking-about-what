<template>
    <div>
         <h1> {{ "num1="+num1 }}</h1>
         <h1> {{ "num2="+num2 }}</h1>
         <h1> {{ "num3="+num3 }}</h1>
         <h1> {{ "num4="+num4 }}</h1>
         <h1> {{ "num5="+0 }}</h1>
         <div @click="addnum" class="btn">+</div>
         <h1>{{num6}}</h1>
         <h1>{{ num7.name }}</h1>
    </div>
</template>

<script>
    export default {
        name: 'VueTest',
        data() {
            return {
                num1:1,
                num2:3,
                num3:4,
                num4:5,
                num5:0,
                num6:['1'],
                num7:{name:'软件专业'}
            }
        },
        computed: {
            js:function() {
                return this.num1 + this.num2 + this.num3 + this.num4
            }
        },
        methods: {
            addnum() {
                this.num1++
                this.num6.push('1')
                this.num7.name += '好'
            }
        },
        watch: {
            num1: {
                handler(newvalue, oldvalue) {
                console.log("newvalue="+newvalue)
                console.log("oldvalue="+oldvalue)
            }
        }
    },
    created(){
            console.log(document.createElement('btn')[0])
        },
        mounted(){
            console.log(document.createElement('btn')[0])
    },
}
</script>

<style>
.btn { 
  width:100px ; 
  height:100px;   
  color:red; 
  background-color: green;
  font-size: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  }
  
</style>