/* @odoo-module */
import { registry} from '@web/core/registry';
import { Workshop } from './workshop.js'

const { Component, mount} = owl
export class AdvancedDashboard extends Component {

}
AdvancedDashboard.template = "client_action.advanced_dashboard"
AdvancedDashboard.components = {Workshop}
registry.category("actions").add("advanced_dashboard", AdvancedDashboard)