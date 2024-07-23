import { ServiceFactory } from "./servicefactory";
import { getConfig } from "./task/register";

export function initializeServices() {
	const applicationMode = 'prod';
	// const applicationMode = 'dev';
	const taskConfig = getConfig(applicationMode);
	ServiceFactory.register(taskConfig.interfaceType, taskConfig.service);
}