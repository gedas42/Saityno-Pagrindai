import { mount } from "@vue/test-utils";
import HelloWorld from "../components/HelloWorld.vue";
import { describe, it, expect } from "vitest";

describe("HelloWorld.vue", () => {

    it("should render the page correctly", () => {
        const message = "Happy People";
        const testMessage = "Happy People";
        const wrapper = mount(HelloWorld, {
            propsData: { message },
        });

        expect(wrapper.text()).toBe(testMessage);
    });

    it("should render the page correctly with empty props", () => {
        const testMessage = "World";
        const wrapper = mount(HelloWorld, {
        });

        expect(wrapper.vm.message).toBe(testMessage);
    });
});