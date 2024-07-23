import { MockTaskService } from "./mocktaskservice";
import { TaskService, ITaskService } from "./taskservice";

export function getConfig(applicationMode: string) {
	if (applicationMode == 'dev') {
		return { interfaceType: ITaskService, service: new MockTaskService() }
	}

	return { interfaceType: ITaskService, service: new TaskService() }
}