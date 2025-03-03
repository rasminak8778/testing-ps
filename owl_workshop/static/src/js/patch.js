/* @odoo-module */
import { AdvancedDashboard } from './owl_workshop';
import { patch } from "@web/core/utils/patch";

patch(AdvancedDashboard.prototype, {
    setup(){
        super.setup()
        this.DemoFunction()
//        this.data = 1
    },
//    handleButtonClick(){
//        console.log('clickingggg')
//    },
    DemoFunction(){
        console.log('aaaaaaaaaa',this)
    }
});