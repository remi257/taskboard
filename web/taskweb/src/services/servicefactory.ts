import type { Type } from "typescript";

export class ServiceFactory {
	private static _services = new Map<any, IService>;

	public static register<T extends IService>(interfaceType: Function, service: T) {
		this._services.set(interfaceType, service);
	}

	public static get<S extends IService>(interfaceType: Function): S {
		return this._services.get(interfaceType) as S;
	}

	private constructor() {

	}
}

export abstract class IService {
	// public static getName();
}

export function getService<S extends IService>(interfaceType: Function): S {
	return ServiceFactory.get(interfaceType);
}

